from flask import Flask, render_template, request, send_file, after_this_request, jsonify, redirect, url_for, flash, Response
from config import Config
import os
import uuid
import zipfile
import subprocess
import json as json_mod
from io import BytesIO
from utils.pdf_generator import (
    generate_odluka_pdf,
    generate_statut_pdf,
    generate_odluka_pdf_višečlano,
    generate_statut_pdf_višečlano
)
from utils.wiki_reader import (
    WikiReader, resolve_wiki_link, WIKI_CATEGORIES,
    save_uploaded_file, get_unprocessed_sources, get_upload_queue,
    update_queue_item, remove_from_queue, ALLOWED_EXTENSIONS,
    get_raw_sources_path
)
from utils.kd_reader import KDReader, get_kd_reader

import datetime
app = Flask(__name__)
app.config.from_object(Config)

# Initialize wiki reader
wiki_reader = WikiReader(app.config['WIKI_PATH'])


# ─── Context processor: make wiki categories available in all templates ───

@app.context_processor
def inject_wiki_nav():
    return {
        "wiki_categories": wiki_reader.get_categories(),
        "wiki_path": app.config['WIKI_PATH'],
    }


# ─── Home ────────────────────────────────────────────────────────────────

@app.route('/')
def home():
    return render_template('home.html')


# ─── Wiki Explorer ───────────────────────────────────────────────────────

@app.route('/wiki')
def wiki_index():
    """Wiki home page — shows all categories and pages."""
    categories = wiki_reader.get_categories()
    stats = wiki_reader.get_stats()
    return render_template('wiki.html', categories=categories, stats=stats, view='index')


@app.route('/wiki/<category>/<slug>')
def wiki_page(category, slug):
    """View a single wiki page."""
    page = wiki_reader.get_page(category, slug)
    if not page:
        flash(f"Stranica nije pronađena: {category}/{slug}", "error")
        return redirect(url_for('wiki_index'))

    raw_content = wiki_reader.get_raw_content(category, slug)
    backlinks = wiki_reader.get_backlinks(category, slug)

    # Resolve wiki links to check which are valid
    resolved_links = []
    for link in page.get("wiki_links", []):
        resolved = resolve_wiki_link(link, wiki_reader)
        resolved_links.append({
            "slug": link,
            "valid": resolved is not None,
            "page": resolved,
        })

    return render_template(
        'wiki.html',
        categories=wiki_reader.get_categories(),
        page=page,
        page_content=raw_content,
        backlinks=backlinks,
        resolved_links=resolved_links,
        category=category,
        slug=slug,
        view='page',
    )


@app.route('/wiki/<category>/<slug>/edit', methods=['GET', 'POST'])
def wiki_edit(category, slug):
    """Edit a wiki page."""
    if request.method == 'POST':
        content = request.form.get('content', '')
        wiki_reader.save_page(category, slug, content)

        # Run verify-index.py
        scripts_dir = os.path.join(os.path.expanduser('~'), 'agera-knowledge', 'scripts')
        verify_script = os.path.join(scripts_dir, 'verify-index.py')
        validation_result = None
        if os.path.exists(verify_script):
            try:
                result = subprocess.run(
                    ['python3', verify_script],
                    capture_output=True, text=True, timeout=30
                )
                validation_result = {
                    "success": result.returncode == 0,
                    "output": result.stdout + result.stderr,
                }
            except Exception as e:
                validation_result = {"success": False, "output": str(e)}

        if request.headers.get('HX-Request'):
            return render_template(
                'partials/edit_result.html',
                validation=validation_result,
                category=category,
                slug=slug,
            )

        flash("Stranica je sačuvana.", "success")
        return redirect(url_for('wiki_page', category=category, slug=slug))

    # GET — show editor
    raw_content = wiki_reader.get_raw_content(category, slug)
    if raw_content is None:
        flash(f"Stranica nije pronađena: {category}/{slug}", "error")
        return redirect(url_for('wiki_index'))

    page = wiki_reader.get_page(category, slug)
    return render_template(
        'wiki.html',
        categories=wiki_reader.get_categories(),
        page=page,
        page_content=raw_content,
        category=category,
        slug=slug,
        view='edit',
    )


@app.route('/wiki/search')
def wiki_search():
    """Search results page (server-side rendered)."""
    query = request.args.get('q', '')
    results = []
    if query:
        raw_results = wiki_reader.search(query, limit=20)
        for r in raw_results:
            page = r["page"]
            page["category_slug"] = page.get("category_slug", "")
            # Try to determine category from file path
            if not page["category_slug"]:
                for cat in WIKI_CATEGORIES:
                    if wiki_reader.get_page(cat, page["slug"]):
                        page["category_slug"] = cat
                        break
            results.append({
                "page": page,
                "snippet": r["snippet"],
                "score": r["score"],
            })
    return render_template(
        'wiki.html',
        view='search',
        query=query,
        results=results,
    )


@app.route('/wiki/go')
def wiki_go():
    """Quick navigation — find a page by slug and redirect."""
    slug = request.args.get('slug', '') or request.args.get('q', '')
    if not slug:
        return redirect(url_for('wiki_index'))
    # Search across all categories
    for cat in WIKI_CATEGORIES:
        page = wiki_reader.get_page(cat, slug)
        if page:
            return redirect(url_for('wiki_page', category=cat, slug=slug))
    # Fuzzy: try search
    results = wiki_reader.search(slug, limit=1)
    if results:
        page = results[0]["page"]
        cat = page.get("category_slug", "")
        if not cat:
            for c in WIKI_CATEGORIES:
                if wiki_reader.get_page(c, page["slug"]):
                    cat = c
                    break
        if cat:
            return redirect(url_for('wiki_page', category=cat, slug=page["slug"]))
    flash(f"Stranica nije pronađena: {slug}", "error")
    return redirect(url_for('wiki_index'))


@app.route('/api/wiki/page/<category>/<slug>')
def wiki_page_api(category, slug):
    """Get page content as JSON."""
    content = wiki_reader.get_raw_content(category, slug)
    if content is None:
        return jsonify({"error": "not found"}), 404
    return jsonify({"content": content})


@app.route('/wiki/new', methods=['GET', 'POST'])
def wiki_new():
    """Create a new wiki page."""
    if request.method == 'POST':
        category = request.form.get('category', 'concepts')
        slug = request.form.get('slug', '').strip().lower().replace(' ', '-')
        title = request.form.get('title', slug)
        content = request.form.get('content', '')

        if not slug:
            flash("Slug je obavezan.", "error")
            return redirect(url_for('wiki_new'))

        # Pre-fill with template
        if not content:
            content = f"# [[{slug}]] - {title}\n\n"
            content += f"> **Type:** {category[:-1] if category.endswith('s') else category}\n"
            content += f"> **Last updated:** {__import__('datetime').date.today().isoformat()}\n\n"
            content += "## 📋 Sažetak\n\n\n\n"
            content += "## 🔍 Detalji\n\n\n\n"
            content += "## 🔗 Povezani koncepti\n\n\n\n"
            content += "## 📚 Izvori\n\n\n"

        wiki_reader.save_page(category, slug, content)
        flash(f"Stranica kreirana: {category}/{slug}", "success")
        return redirect(url_for('wiki_page', category=category, slug=slug))

    return render_template(
        'wiki.html',
        categories=wiki_reader.get_categories(),
        view='new',
        wiki_categories=WIKI_CATEGORIES,
    )


# ─── Wiki API ────────────────────────────────────────────────────────────

@app.route('/api/wiki/search')
def wiki_search_api():
    """Search wiki pages. Returns JSON."""
    query = request.args.get('q', '')
    limit = int(request.args.get('limit', 20))
    results = wiki_reader.search(query, limit=limit)
    return jsonify({
        "query": query,
        "count": len(results),
        "results": [
            {
                "title": r["page"]["title"],
                "slug": r["page"]["slug"],
                "category": r["page"].get("category_slug", ""),
                "snippet": r["snippet"],
                "score": r["score"],
            }
            for r in results
        ],
    })


@app.route('/api/wiki/stats')
def wiki_stats_api():
    """Wiki statistics. Returns JSON."""
    return jsonify(wiki_reader.get_stats())


@app.route('/api/wiki/validate-links')
def wiki_validate_links():
    """Run verify-index.py and return results."""
    scripts_dir = os.path.join(os.path.expanduser('~'), 'agera-knowledge', 'scripts')
    verify_script = os.path.join(scripts_dir, 'verify-index.py')
    if os.path.exists(verify_script):
        result = subprocess.run(
            ['python3', verify_script],
            capture_output=True, text=True, timeout=30
        )
        return jsonify({
            "valid": result.returncode == 0,
            "output": result.stdout + result.stderr,
        })
    return jsonify({"valid": False, "output": "verify-index.py not found"})


@app.route('/api/wiki/regenerate-index')
def wiki_regenerate_index():
    """Run regenerate-index.py."""
    scripts_dir = os.path.join(os.path.expanduser('~'), 'agera-knowledge', 'scripts')
    regen_script = os.path.join(scripts_dir, 'regenerate-index.py')
    if os.path.exists(regen_script):
        result = subprocess.run(
            ['python3', regen_script],
            capture_output=True, text=True, timeout=30
        )
        return jsonify({
            "success": result.returncode == 0,
            "output": result.stdout + result.stderr,
        })
    return jsonify({"success": False, "output": "regenerate-index.py not found"})


# ─── Source Upload & Ingest Queue ─────────────────────────────────────────

@app.route('/wiki/upload', methods=['GET'])
def wiki_upload_page():
    """Upload page — drag & drop zone + queue."""
    base_path = os.path.join(os.path.expanduser('~'), 'agera-knowledge')
    queue = get_upload_queue(base_path)
    unprocessed = get_unprocessed_sources(base_path)
    return render_template(
        'wiki.html',
        view='upload',
        queue=queue,
        unprocessed=unprocessed,
        allowed_extensions=sorted(ALLOWED_EXTENSIONS),
    )


@app.route('/api/wiki/upload', methods=['POST'])
def wiki_upload_api():
    """Handle file upload. Saves to raw-sources/ and adds to queue."""
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    # Check extension
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return jsonify({"error": f"File type not allowed: {ext}"}), 400

    # Read file bytes
    file_bytes = file.read()
    if len(file_bytes) == 0:
        return jsonify({"error": "Empty file"}), 400

    # Max 50MB
    if len(file_bytes) > 50 * 1024 * 1024:
        return jsonify({"error": "File too large (max 50MB)"}), 400

    base_path = os.path.join(os.path.expanduser('~'), 'agera-knowledge')
    result = save_uploaded_file(base_path, file_bytes, file.filename)

    return jsonify(result)


@app.route('/api/wiki/queue', methods=['GET'])
def wiki_queue_api():
    """Get current upload queue."""
    base_path = os.path.join(os.path.expanduser('~'), 'agera-knowledge')
    return jsonify({
        "queue": get_upload_queue(base_path),
        "unprocessed": get_unprocessed_sources(base_path),
    })


@app.route('/api/wiki/queue/<item_id>', methods=['DELETE'])
def wiki_queue_remove_api(item_id):
    """Remove an item from the queue."""
    base_path = os.path.join(os.path.expanduser('~'), 'agera-knowledge')
    if remove_from_queue(base_path, item_id):
        return jsonify({"success": True})
    return jsonify({"error": "Item not found"}), 404


@app.route('/api/wiki/queue/<item_id>/status', methods=['PUT'])
def wiki_queue_status_api(item_id):
    """Update queue item status."""
    data = request.get_json(silent=True) or {}
    base_path = os.path.join(os.path.expanduser('~'), 'agera-knowledge')
    if update_queue_item(base_path, item_id, **data):
        return jsonify({"success": True})
    return jsonify({"error": "Item not found"}), 404


@app.route('/api/wiki/sources', methods=['GET'])
def wiki_sources_api():
    """List all files in raw-sources/ with their ingest status."""
    base_path = os.path.join(os.path.expanduser('~'), 'agera-knowledge')
    return jsonify({
        "sources": get_unprocessed_sources(base_path),
    })


# ─── KD 2025 API ───────────────────────────────────────────────────────────

@app.route('/api/kd/search')
def kd_search_api():
    """Search KD 2025 codes by query string."""
    query = request.args.get('q', '')
    sector = request.args.get('sector', None)
    limit = int(request.args.get('limit', 20))
    kd = get_kd_reader()
    results = kd.search(query, limit=limit, sector=sector)
    return jsonify({
        "query": query,
        "count": len(results),
        "results": results,
    })


@app.route('/api/kd/code/<code>')
def kd_code_api(code):
    """Get a single KD code's full details."""
    kd = get_kd_reader()
    entry = kd.get_by_code(code)
    if entry:
        return jsonify(entry)
    return jsonify({"error": "Code not found", "code": code}), 404


@app.route('/api/kd/sectors')
def kd_sectors_api():
    """List all KD sectors with their code counts."""
    kd = get_kd_reader()
    sectors = kd.get_sectors()
    return jsonify({
        "count": len(sectors),
        "sectors": sectors,
    })


@app.route('/api/kd/validate')
def kd_validate_api():
    """Validate one or more KD codes. Pass ?code=xx.xx or ?codes=xx.xx,yy.yy"""
    code = request.args.get('code', '')
    codes_str = request.args.get('codes', '')
    kd = get_kd_reader()

    if code:
        valid = kd.validate(code.strip())
        return jsonify({"code": code.strip(), "valid": valid})

    if codes_str:
        codes = [c.strip() for c in codes_str.split(',') if c.strip()]
        results = {c: kd.validate(c) for c in codes}
        return jsonify({"codes": results, "valid_count": sum(results.values())})

    return jsonify({"error": "Provide ?code= or ?codes="}), 400


# ─── Document Generator (existing) ───────────────────────────────────────

@app.route('/form/doo-jednočlano', methods=['GET', 'POST'])
def form_doo_jednočlano():
    if request.method == 'POST':
        data = {
            'osnivač_ime': request.form.get('osnivač_ime'),
            'osnivač_jmbg': request.form.get('osnivač_jmbg'),
            'osnivač_adresa': request.form.get('osnivač_adresa'),
            'osnivač_drzavljanstvo': request.form.get('osnivač_drzavljanstvo'),
            'društvo_naziv': request.form.get('društvo_naziv'),
            'društvo_adresa': request.form.get('društvo_adresa'),
            'društvo_kd': request.form.get('društvo_kd'),
            'društvo_kd_ostali': request.form.get('društvo_kd_ostali', ''),
            'društvo_kapital': request.form.get('društvo_kapital'),
            'direktor_ime': request.form.get('direktor_ime'),
            'direktor_jmbg': request.form.get('direktor_jmbg'),
            'datum_danas': request.form.get('datum_danas') or '2026-05-08',
        }
        session_id = str(uuid.uuid4())[:8]
        odluka_pdf = generate_odluka_pdf(data, session_id)
        statut_pdf = generate_statut_pdf(data, session_id)
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.write(odluka_pdf, f"odluka-o-osnivanju-{data['društvo_naziv'].lower().replace(' ', '-')}.pdf")
            zf.write(statut_pdf, f"statut-doo-jednočlano-{data['društvo_naziv'].lower().replace(' ', '-')}.pdf")
        zip_buffer.seek(0)

        @after_this_request
        def cleanup(response):
            try:
                os.remove(odluka_pdf)
                os.remove(statut_pdf)
            except:
                pass
            return response

        return send_file(
            zip_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name=f"dokumenta-doo-{session_id}.zip"
        )

    return render_template('form-doo-jednočlano.html')


@app.route('/form/doo-višečlano', methods=['GET', 'POST'])
def form_doo_višečlano():
    if request.method == 'POST':
        osnivači = []
        i = 0
        while f'osnivač_{i}_ime' in request.form:
            osnivači.append({
                'ime': request.form.get(f'osnivač_{i}_ime'),
                'jmbg': request.form.get(f'osnivač_{i}_jmbg'),
                'adresa': request.form.get(f'osnivač_{i}_adresa'),
                'drzavljanstvo': request.form.get(f'osnivač_{i}_drzavljanstvo'),
                'procenat': int(request.form.get(f'osnivač_{i}_procenat') or 0)
            })
            i += 1
        direktori = []
        i = 0
        while f'direktor_{i}_ime' in request.form:
            direktori.append({
                'ime': request.form.get(f'direktor_{i}_ime'),
                'jmbg': request.form.get(f'direktor_{i}_jmbg')
            })
            i += 1
        data = {
            'osnivači': osnivači,
            'društvo_naziv': request.form.get('društvo_naziv'),
            'društvo_adresa': request.form.get('društvo_adresa'),
            'društvo_kd': request.form.get('društvo_kd'),
            'društvo_kapital': int(request.form.get('društvo_kapital') or 1),
            'direktori': direktori,
            'skupština_predsjednik': request.form.get('skupština_predsjednik'),
            'skupština_zapisničar': request.form.get('skupština_zapisničar'),
            'datum_danas': request.form.get('datum_danas') or '2026-05-08',
        }
        session_id = str(uuid.uuid4())[:8]
        odluka_pdf = generate_odluka_pdf_višečlano(data, session_id)
        statut_pdf = generate_statut_pdf_višečlano(data, session_id)
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.write(odluka_pdf, f"odluka-o-osnivanju-{data['društvo_naziv'].lower().replace(' ', '-')}.pdf")
            zf.write(statut_pdf, f"statut-doo-višečlano-{data['društvo_naziv'].lower().replace(' ', '-')}.pdf")
        zip_buffer.seek(0)

        @after_this_request
        def cleanup(response):
            try:
                os.remove(odluka_pdf)
                os.remove(statut_pdf)
            except:
                pass
            return response

        return send_file(
            zip_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name=f"dokumenta-doo-{session_id}.zip"
        )

    return render_template('form-doo-višečlano.html')



# ─── Health Check ────────────────────────────────────────────────────────────

@app.route('/api/health')
def health_check():
    """Health endpoint for monitoring and uptime checks."""
    return jsonify({
        'status': 'ok',
        'service': 'agera-document-portal',
        'timestamp': datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
