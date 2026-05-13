"""
AGERA Wiki Reader — utilities for reading and serving wiki pages.
"""
import os
import re
import json
import hashlib
from pathlib import Path
from typing import Optional
from datetime import datetime

# Wiki categories and their display names
WIKI_CATEGORIES = {
    "concepts": "Koncepti",
    "legislation": "Legislativa",
    "services": "Usluge",
    "processes": "Procesi",
    "raw-sources": "Izvori",
    "clients": "Klijenti",
    "software-tools": "Alati",
    "templates": "Šabloni",
}

# Category icons
CATEGORY_ICONS = {
    "concepts": "fa-lightbulb",
    "legislation": "fa-scale-balanced",
    "services": "fa-briefcase",
    "processes": "fa-diagram-project",
    "raw-sources": "fa-file-lines",
    "clients": "fa-users",
    "software-tools": "fa-wrench",
    "templates": "fa-file-code",
}


class WikiReader:
    def __init__(self, wiki_path: str):
        self.wiki_path = Path(wiki_path)
        self._pages_cache = {}
        self._search_index = None

    def get_categories(self) -> list[dict]:
        """Return list of categories with their pages."""
        categories = []
        for slug, name in WIKI_CATEGORIES.items():
            cat_path = self.wiki_path / slug
            if not cat_path.exists():
                continue
            pages = []
            for f in sorted(cat_path.glob("*.md")):
                page_info = self._get_page_info(f)
                pages.append(page_info)
            if pages:
                categories.append({
                    "slug": slug,
                    "name": name,
                    "icon": CATEGORY_ICONS.get(slug, "fa-folder"),
                    "pages": pages,
                    "count": len(pages),
                })
        return categories

    def get_page(self, category: str, slug: str) -> Optional[dict]:
        """Get a single wiki page by category and slug."""
        # Handle subdirectories (e.g., pdf/)
        file_path = self.wiki_path / category / f"{slug}.md"
        if not file_path.exists():
            return None
        return self._get_page_info(file_path)

    def get_page_by_path(self, path: str) -> Optional[dict]:
        """Get a page by relative path like 'concepts/pdv'."""
        parts = path.split("/", 1)
        if len(parts) == 2:
            return self.get_page(parts[0], parts[1])
        return None

    def get_raw_content(self, category: str, slug: str) -> Optional[str]:
        """Get raw markdown content of a page."""
        file_path = self.wiki_path / category / f"{slug}.md"
        if not file_path.exists():
            return None
        return file_path.read_text(encoding="utf-8")

    def save_page(self, category: str, slug: str, content: str) -> bool:
        """Save (overwrite) a wiki page."""
        cat_path = self.wiki_path / category
        cat_path.mkdir(parents=True, exist_ok=True)
        file_path = cat_path / f"{slug}.md"
        file_path.write_text(content, encoding="utf-8")
        # Invalidate cache
        cache_key = f"{category}/{slug}"
        self._pages_cache.pop(cache_key, None)
        self._search_index = None
        return True

    def get_all_pages(self) -> list[dict]:
        """Flat list of all wiki pages."""
        pages = []
        for slug in WIKI_CATEGORIES:
            cat_path = self.wiki_path / slug
            if not cat_path.exists():
                continue
            for f in sorted(cat_path.glob("*.md")):
                page_info = self._get_page_info(f)
                page_info["category_slug"] = slug
                pages.append(page_info)
        return pages

    def search(self, query: str, limit: int = 20) -> list[dict]:
        """Full-text search across all wiki pages."""
        if not query or len(query) < 2:
            return []

        query_lower = query.lower()
        results = []

        for page in self.get_all_pages():
            content = self.get_raw_content(page["category_slug"], page["slug"])
            if content is None:
                continue

            content_lower = content.lower()
            score = 0

            # Title match (highest weight)
            if query_lower in page["title"].lower():
                score += 10
            if page["title"].lower().startswith(query_lower):
                score += 5

            # Content match
            count = content_lower.count(query_lower)
            score += count

            # Header match
            for line in content.split("\n"):
                if line.startswith("#") and query_lower in line.lower():
                    score += 3

            if score > 0:
                # Extract snippet
                snippet = self._extract_snippet(content, query)
                results.append({
                    "page": page,
                    "score": score,
                    "snippet": snippet,
                })

        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:limit]

    def get_stats(self) -> dict:
        """Get wiki statistics."""
        total_pages = 0
        category_counts = {}
        for slug, name in WIKI_CATEGORIES.items():
            cat_path = self.wiki_path / slug
            if not cat_path.exists():
                continue
            count = len(list(cat_path.glob("*.md")))
            category_counts[slug] = {"name": name, "count": count}
            total_pages += count

        # Count broken links
        broken_links = self._find_broken_links()

        # Recent ingests from logs
        logs_path = self.wiki_path.parent / "logs"
        recent_logs = []
        if logs_path.exists():
            log_files = sorted(logs_path.glob("*.md"), reverse=True)[:5]
            for lf in log_files:
                recent_logs.append({
                    "file": lf.name,
                    "date": lf.stem.split("-")[-1] if "-" in lf.stem else "",
                })

        return {
            "total_pages": total_pages,
            "categories": category_counts,
            "broken_links_count": len(broken_links),
            "broken_links": broken_links[:20],  # Limit for display
            "recent_logs": recent_logs,
        }

    def get_backlinks(self, category: str, slug: str) -> list[dict]:
        """Find all pages that link to this page."""
        target = f"{slug}"
        backlinks = []
        for page in self.get_all_pages():
            if page["category_slug"] == category and page["slug"] == slug:
                continue
            content = self.get_raw_content(page["category_slug"], page["slug"])
            if content and f"[[{target}]]" in content:
                backlinks.append(page)
        return backlinks

    # --- Internal methods ---

    def _get_page_info(self, file_path: Path) -> dict:
        """Extract metadata from a wiki page file."""
        cache_key = str(file_path)
        if cache_key in self._pages_cache:
            return self._pages_cache[cache_key]

        content = file_path.read_text(encoding="utf-8")
        slug = file_path.stem

        # Extract title from first # heading
        title = slug
        for line in content.split("\n"):
            if line.startswith("# "):
                title = line[2:].strip()
                # Remove [[slug]] prefix from title
                title = re.sub(r"\[\[([^\]]+)\]\]\s*[-–—]?\s*", "", title).strip()
                if not title:
                    title = slug
                break

        # Extract type and category from frontmatter-style metadata
        page_type = ""
        for line in content.split("\n"):
            if line.startswith("> **Type:**"):
                page_type = line.split(":", 1)[1].strip()
                break

        # Extract summary
        summary = ""
        in_summary = False
        for line in content.split("\n"):
            if "##" in line and ("Sažetak" in line or "Saetak" in line):
                in_summary = True
                continue
            if in_summary:
                if line.startswith("##"):
                    break
                if line.strip() and not line.startswith(">"):
                    summary = line.strip()
                    break

        # Extract wiki links
        wiki_links = re.findall(r"\[\[([^\]]+)\]\]", content)

        info = {
            "slug": slug,
            "title": title,
            "type": page_type,
            "summary": summary,
            "wiki_links": wiki_links,
            "file_path": str(file_path),
            "file_name": file_path.name,
            "size": file_path.stat().st_size,
        }
        self._pages_cache[cache_key] = info
        return info

    def _extract_snippet(self, content: str, query: str, context: int = 80) -> str:
        """Extract a snippet around the query match."""
        idx = content.lower().find(query.lower())
        if idx == -1:
            # Return first non-empty, non-heading line
            for line in content.split("\n"):
                stripped = line.strip()
                if stripped and not stripped.startswith("#") and not stripped.startswith(">"):
                    return stripped[:200]
            return content[:200].strip()

        start = max(0, idx - context)
        end = min(len(content), idx + len(query) + context)
        snippet = content[start:end].strip()

        # Clean up
        if start > 0:
            snippet = "..." + snippet
        if end < len(content):
            snippet = snippet + "..."

        # Remove markdown artifacts
        snippet = re.sub(r"\[\[([^\]]+)\]\]", r"\1", snippet)
        snippet = snippet.replace("#", "").replace(">", "").strip()

        return snippet[:300]

    def _find_broken_links(self) -> list[dict]:
        """Find all broken wiki links."""
        broken = []
        all_slugs = set()
        for slug in WIKI_CATEGORIES:
            cat_path = self.wiki_path / slug
            if cat_path.exists():
                for f in cat_path.glob("*.md"):
                    all_slugs.add(f.stem)

        for page in self.get_all_pages():
            content = self.get_raw_content(page["category_slug"], page["slug"])
            if not content:
                continue
            links = re.findall(r"\[\[([^\]]+)\]\]", content)
            for link in links:
                if link not in all_slugs:
                    broken.append({
                        "source": f"{page['category_slug']}/{page['slug']}",
                        "target": link,
                    })
        return broken


def resolve_wiki_link(link: str, reader: WikiReader) -> Optional[dict]:
    """Resolve a [[wiki-link]] to a page dict, or None if not found."""
    # Try direct match in each category
    for cat_slug in WIKI_CATEGORIES:
        page = reader.get_page(cat_slug, link)
        if page:
            page["category_slug"] = cat_slug
            return page
    return None


# ─── Source Upload & Ingest Queue ─────────────────────────────────────────

# Allowed file extensions for upload
ALLOWED_EXTENSIONS = {".pdf", ".txt", ".md", ".docx", ".csv", ".json", ".html"}

# Map file types to ingest category hints
FILE_TYPE_HINTS = {
    ".pdf": "PDF dokument",
    ".txt": "Tekstualni dokument",
    ".md": "Markdown dokument",
    ".docx": "Word dokument",
    ".csv": "CSV podaci",
    ".json": "JSON podaci",
    ".html": "HTML dokument",
}

# Tracking file for upload queue (JSON)
QUEUE_FILE_NAME = ".upload_queue.json"


def get_upload_queue(base_path: str) -> list[dict]:
    """Get the current upload queue."""
    queue_path = Path(base_path) / QUEUE_FILE_NAME
    if queue_path.exists():
        try:
            data = json.loads(queue_path.read_text(encoding="utf-8"))
            return data.get("queue", [])
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_upload_queue(base_path: str, queue: list[dict]):
    """Save the upload queue."""
    queue_path = Path(base_path) / QUEUE_FILE_NAME
    queue_path.write_text(
        json.dumps({"queue": queue, "updated": datetime.now().isoformat()}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def add_to_queue(base_path: str, filename: str, file_size: int, file_hash: str, category_hint: str = "") -> dict:
    """Add an uploaded file to the ingest queue."""
    queue = get_upload_queue(base_path)

    # Check for duplicates
    for item in queue:
        if item.get("file_hash") == file_hash:
            return {"status": "duplicate", "item": item}

    item = {
        "id": f"upload-{datetime.now().strftime('%Y%m%d%H%M%S')}-{file_hash[:8]}",
        "filename": filename,
        "file_size": file_size,
        "file_hash": file_hash,
        "category_hint": category_hint,
        "status": "pending",  # pending | processing | done | error
        "uploaded_at": datetime.now().isoformat(),
        "processed_at": None,
        "result": None,
        "error": None,
    }
    queue.append(item)
    save_upload_queue(base_path, queue)
    return {"status": "added", "item": item}


def update_queue_item(base_path: str, item_id: str, **kwargs) -> bool:
    """Update a queue item (status, result, error, etc.)."""
    queue = get_upload_queue(base_path)
    for item in queue:
        if item["id"] == item_id:
            item.update(kwargs)
            save_upload_queue(base_path, queue)
            return True
    return False


def remove_from_queue(base_path: str, item_id: str) -> bool:
    """Remove an item from the queue."""
    queue = get_upload_queue(base_path)
    new_queue = [item for item in queue if item["id"] != item_id]
    if len(new_queue) < len(queue):
        save_upload_queue(base_path, new_queue)
        return True
    return False


def get_raw_sources_path(base_path: str) -> Path:
    """Get the raw-sources directory path."""
    return Path(base_path) / "raw-sources"


def save_uploaded_file(base_path: str, file_bytes: bytes, filename: str) -> dict:
    """Save an uploaded file to raw-sources/ and add to queue."""
    raw_sources = get_raw_sources_path(base_path)
    raw_sources.mkdir(parents=True, exist_ok=True)

    # Sanitize filename
    safe_name = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)
    file_path = raw_sources / safe_name

    # Check if file already exists
    file_hash = hashlib.md5(file_bytes).hexdigest()
    if file_path.exists():
        existing_hash = hashlib.md5(file_path.read_bytes()).hexdigest()
        if existing_hash == file_hash:
            return {"status": "duplicate", "path": str(file_path)}

    # Save file
    file_path.write_bytes(file_bytes)

    # Add to queue
    ext = Path(filename).suffix.lower()
    category_hint = FILE_TYPE_HINTS.get(ext, "Nepoznat tip")
    queue_result = add_to_queue(str(Path(base_path)), filename, len(file_bytes), file_hash, category_hint)

    return {
        "status": queue_result["status"],
        "path": str(file_path),
        "queue_item": queue_result.get("item"),
    }


def get_unprocessed_sources(base_path: str) -> list[dict]:
    """Get list of files in raw-sources/ with their ingest status.

    A source is considered "done" if any wiki page (in any category)
    contains the source filename or a significant part of it.
    """
    raw_sources = get_raw_sources_path(base_path)
    if not raw_sources.exists():
        return []

    queue = get_upload_queue(base_path)
    processed_hashes = {item.get("file_hash") for item in queue if item.get("status") == "done"}

    # Build index: for each raw source, extract key tokens (words > 3 chars)
    # Then check if any wiki page content contains those tokens
    wiki_base = Path(base_path) / "wiki"

    # Pre-build a set of all wiki page content (lowercased) for searching
    wiki_content_text = {}  # slug -> lowercased content
    for cat in WIKI_CATEGORIES:
        cat_path = wiki_base / cat
        if not cat_path.exists():
            continue
        for md_file in cat_path.glob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8").lower()
                wiki_content_text[md_file.stem] = content
            except IOError:
                pass

    unprocessed = []
    for f in sorted(raw_sources.iterdir()):
        if f.is_file() and not f.name.startswith("."):
            file_hash = hashlib.md5(f.read_bytes()).hexdigest()
            is_in_queue = file_hash in processed_hashes

            # Check if any wiki page references this source
            src_name_lower = f.name.lower()
            src_stem_lower = f.stem.lower()

            has_wiki_page = False
            for slug, content in wiki_content_text.items():
                # Direct filename match in content
                if src_name_lower in content or src_stem_lower in content:
                    has_wiki_page = True
                    break
                # Check if key tokens from source name appear in content
                # Extract meaningful words (>3 chars, skip common words)
                skip_words = {'the', 'and', 'for', 'pdf', 'doc', 'docx', 'txt', 'this', 'that', 'with', 'from', 'into', 'about', 'o', 'na', 'za', 'i', 'u', 'iz', 'sa', 'po', 'do', 'od', 'za', 'su', 'se', 'ne', 'da', 'je', 'kao', 'ali', 'ili', 'ako', 'kod', 'preko', 'bez', 'nakon', 'prije', 'tokom', 'zbog', 'uprkos', 'protiv', 'izmedju', 'pred', 'pod', 'nad', 'medju'}
                # Extract words from source filename
                import re as _re
                words = _re.findall(r'[a-z0-9]{4,}', src_stem_lower)
                meaningful = [w for w in words if w not in skip_words]
                # If 2+ meaningful words match, consider it processed
                if len(meaningful) >= 2:
                    matches = sum(1 for w in meaningful if w in content)
                    if matches >= 2 or (matches >= 1 and len(meaningful) <= 3):
                        has_wiki_page = True
                        break

            is_done = has_wiki_page or is_in_queue

            ext = f.suffix.lower()
            unprocessed.append({
                "filename": f.name,
                "path": str(f),
                "size": f.stat().st_size,
                "size_human": _format_size(f.stat().st_size),
                "type": FILE_TYPE_HINTS.get(ext, ext),
                "modified": datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M"),
                "status": "done" if is_done else "pending",
                "file_hash": file_hash,
            })

    return unprocessed


def _format_size(size_bytes: int) -> str:
    """Format file size in human-readable format."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"
