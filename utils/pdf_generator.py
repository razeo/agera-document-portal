import os
import re
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from config import Config
from utils.kd_reader import KDReader
from utils.wiki_reader import WikiReader

def number_to_words(n, lang='sr'):
    """
    Convert number to words in Serbian.
    Handles numbers up to 999,999,999
    """
    ones = ['', 'jedan', 'dva', 'tri', 'četiri', 'pet', 'šest', 'sedam', 'osam', 'devet',
            'deset', 'jedanaest', 'dvanaest', 'trinaest', 'četrnaest', 'petnaest', 
            'šesnaest', 'sedamnaest', 'osamnaest', 'devetnaest']
    tens = ['', '', 'dvadeset', 'trideset', 'četrdeset', 'pedeset', 
            'šezdeset', 'sedamdeset', 'osamdeset', 'devedeset']
    scales = ['', 'hiljada', 'miliona', 'milijardi']
    
    def _convert_chunk(n):
        if n < 20:
            return ones[n]
        elif n < 100:
            return tens[n // 10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
        elif n < 1000:
            h = n // 100
            suffix = 'sto'
            if h == 1:
                prefix = ''
            elif h == 2:
                prefix = 'dvje' if suffix else 'dva'
            else:
                prefix = ones[h]
            remainder = n % 100
            if remainder == 0:
                return (prefix or '') + 'sto'
            else:
                return (prefix or '') + 'sto ' + _convert_chunk(remainder)
        return str(n)
    
    if n == 0:
        return 'nula'
    
    result = []
    scale = 0
    
    while n > 0:
        chunk = n % 1000
        if chunk > 0:
            words = _convert_chunk(chunk)
            if scale > 0 and scale < len(scales):
                result.insert(0, scales[scale])
            result.insert(0, words)
        n //= 1000
        scale += 1
    
    return ' '.join(result)


def _resolve_kd_code(code: str) -> str:
    """Resolve a KD code to 'xx.xx — Full Name' format."""
    if not code or not code.strip():
        return code
    try:
        kd = KDReader()
        formatted = kd.format_for_display(code.strip())
        return formatted if formatted != code.strip() else code
    except Exception:
        return code


def _resolve_kd_codes(codes_str: str, separator: str = ', ') -> str:
    """Resolve a comma-separated list of KD codes to formatted strings."""
    if not codes_str or not codes_str.strip():
        return ''
    codes = [c.strip() for c in codes_str.split(',') if c.strip()]
    resolved = [_resolve_kd_code(c) for c in codes]
    return separator.join(resolved)


def _prepare_data(data: dict) -> dict:
    """Prepare form data for PDF templates: resolve KD codes, add computed fields."""
    data = dict(data)  # Don't mutate original
    data['kapital_slovima'] = number_to_words(int(data.get('društvo_kapital', 0)))

    # Resolve primary KD code — overwrite with full name
    raw_kd = data.get('društvo_kd', '')
    data['društvo_kd_raw'] = raw_kd
    data['društvo_kd'] = _resolve_kd_code(raw_kd)

    # Resolve additional KD codes (comma-separated → list for template)
    raw_ostali = data.get('društvo_kd_ostali', '')
    ostali_list = []
    if raw_ostali and raw_ostali.strip():
        codes = [c.strip() for c in raw_ostali.split(',') if c.strip()]
        ostali_list = [_resolve_kd_code(c) for c in codes]
    data['društvo_kd_ostali_list'] = ostali_list
    data['društvo_kd_ostali'] = '\n'.join(ostali_list)

    # Compute short company name
    naziv = data.get('društvo_naziv', '')
    skraceno = naziv.replace('Društvo sa ograničenom odgovornošću ', '').replace('DOO ', '').strip()
    data['društvo_naziv_skraceno'] = skraceno

    return data


# ─── Wiki Template Engine ─────────────────────────────────────────────────

# Article ordering for statut-doo-jednoclano
STATUT_ARTICLE_ORDER = [
    "osnovne_odredbe",       # Član 1
    "poslovno_ime",          # Član 2
    "sjediste",              # Član 3
    "adresa",                # Član 4
    "pib",                   # Član 5
    "pretezna_djelatnost",   # Član 6
    # "ostale_djelatnosti" inserted here at 7 if has_ostali
    "dozvole",               # Član 7 (or 8 with ostali)
    "osnovni_kapital",       # Član 8 (or 9)
    "udio_osnivaca",         # Član 9 (or 10)
    "prava_iz_udjela",       # Član 10 (or 11)
    "povecanje_smanjenje",   # Član 11 (or 12)
    "organi_drustva",        # Član 12 (or 13)
    "skupstina",             # Član 13 (or 14)
    "nadleznost_skupstine",  # Član 14 (or 15)
    "sjednice_skupstine",    # Član 15 (or 16)
    "direktor_imenovanje",   # Član 16 (or 17)
    "direktor_nadleznost",   # Član 17 (or 18)
    "direktor_odgovornost",  # Član 18 (or 19)
    "direktor_zastupanje",   # Član 19 (or 20)
    "direktor_odsustvo",     # Član 20 (or 21)
    "zastupanje",            # Član 21 (or 22)
    "prokura",               # Član 22 (or 23)
    "odobrenje_ugovori",     # Član 23 (or 24)
    "poslovne_knjige",       # Član 24 (or 25)
    "knjiga_odluka",         # Član 25 (or 26)
    "cuvanje_dokumenata",    # Član 26 (or 27)
    "raspodjela_dobiti",     # Član 27 (or 28)
    "rezerve",               # Član 28 (or 29)
    "prestanak_drustva",     # Član 29 (or 30)
    "stupanje_na_snagu",     # Član 30 (or 31)
    "sacinjavanje",          # Član 31 (or 32)
    "registracija",          # Član 32 (or 33)
]

# Keys that define subchapter breaks (displayed as sub-headings within chapters)
STATUT_SUBCHAPTERS = {
    "skupstina": "1. Skupština Društva",
    "direktor_imenovanje": "2. Direktor Društva",
}

# Offset starts from this article key (inclusive) when has_ostali
STATUT_OFFSET_START_KEY = "dozvole"

# Article ordering for statut-doo-viseclano
STATUT_VISECLANO_ORDER = [
    "osnovne_odredbe",          # Član 1
    "poslovno_ime",             # Član 2
    "sjediste",                 # Član 3
    "adresa",                   # Član 4
    "clanovi_drustva",          # Član 5 (dynamic list)
    "pretezna_djelatnost",      # Član 6
    # "ostale_djelatnosti" inserted here at 7 if has_ostali
    "dozvole",                  # Član 7 (or 8)
    "osnovni_kapital",          # Član 8 (or 9)
    "udjeli_osnivaca",          # Član 9 (or 10) dynamic list
    "povecanje_smanjenje",      # Član 10 (or 11)
    "organi_drustva",           # Član 11 (or 12)
    "skupstina",                # Član 12 (or 13)
    "nadleznost_skupstine",     # Član 13 (or 14)
    "sjednice_skupstine",       # Član 14 (or 15)
    "direktor_imenovanje",      # Član 15 (or 16) dynamic list
    "direktor_nadleznost",      # Član 16 (or 17)
    "direktor_odgovornost",     # Član 17 (or 18)
    "direktor_zastupanje",      # Član 18 (or 19)
    "direktor_odsustvo",        # Član 19 (or 20)
    "zastupanje",               # Član 20 (or 21)
    "prokura",                  # Član 21 (or 22)
    "odobrenje_ugovori",        # Član 22 (or 23)
    "poslovne_knjige",          # Član 23 (or 24)
    "knjiga_odluka",            # Član 24 (or 25)
    "cuvanje_dokumenata",       # Član 25 (or 26)
    "raspodjela_dobiti",        # Član 26 (or 27)
    "rezerve",                  # Član 27 (or 28)
    "prestanak_drustva",        # Član 28 (or 29)
    "stupanje_na_snagu",        # Član 29 (or 30)
    "sacinjavanje",             # Član 30 (or 31)
    "registracija",             # Član 31 (or 32)
]

# Subchapters for višečlano statut
STATUT_VISECLANO_SUBCHAPTERS = {
    "skupstina": "1. Skupština Društva",
    "direktor_imenovanje": "2. Direktor Društva",
}

# Article ordering for odluka-osnivanje-jednoclano
ODLUKA_JEDNOCLANO_ORDER = [
    "osnivac",
    "poslovno_ime",
    "sjediste",
    "djelatnost",
    "osnovni_kapital",
    "udio_osnivaca",
    "direktor",
    "zastupanje",
    "stupanje_na_snagu",
    "zavrsna_odredba",
]

# Article ordering for odluka-osnivanje-viseclano
ODLUKA_VISECLANO_ORDER = [
    "osnivaci",
    "poslovno_ime",
    "sjediste",
    "djelatnost",
    "osnovni_kapital",
    "udjeli_osnivaca",
    "direktori",
    "zastupanje",
    "predsjednik_skupstine",
    "zapisnicar",
    "stupanje_na_snagu",
    "zavrsna_odredba",
]

# Article ordering for odluka-osnivanje-preduzetnik
ODLUKA_PREDUZETNIK_ORDER = [
    "osnovne_odredbe",
    "poslovno_ime",
    "sjediste",
    "djelatnost",
    "podaci_o_preduzetniku",
    "stupanje_na_snagu",
    "zavrsna_odredba",
]

# Poslovodja is a separate article inserted conditionally


def _get_wiki_reader():
    """Get WikiReader instance for the configured wiki path."""
    return WikiReader(Config.WIKI_PATH)


def _load_wiki_template(category: str, slug: str) -> str:
    """Load raw markdown content of a wiki template page."""
    reader = _get_wiki_reader()
    content = reader.get_raw_content(category, slug)
    if content is None:
        raise FileNotFoundError(f"Wiki template not found: {category}/{slug}")
    return content


def _parse_wiki_template(content: str) -> dict:
    """
    Parse a wiki template page into structured components.

    Returns:
        {
            "preamble": "text before first article",
            "articles": {
                "key": {
                    "text": "article content with {placeholders}",
                    "chapter": "Chapter heading or None"
                }
            },
            "chapters": {"key": "Chapter heading"}
        }
    """
    lines = content.split('\n')
    
    preamble_parts = []
    articles = {}
    chapters = {}
    
    current_key = None
    current_chapter = None
    in_preamble = False
    preamble_active = False
    
    for line in lines:
        # Detect preamble section
        if line.strip().startswith('## Preamble'):
            in_preamble = True
            preamble_active = True
            continue
        
        if in_preamble and line.strip().startswith('---'):
            in_preamble = False
            continue
        
        if in_preamble and line.strip():
            preamble_parts.append(line.strip())
            continue
        
        # Detect chapter headings
        if line.strip().startswith('## Chapter:'):
            chapter_text = line.strip()[len('## Chapter:'):].strip()
            current_chapter = chapter_text
            continue
        
        # Detect article keys (### key)
        if line.strip().startswith('### ') and not line.strip().startswith('#### '):
            # Save previous article
            if current_key and current_key in articles:
                pass  # Already handled
            
            key = line.strip()[4:].strip()
            current_key = key
            articles[current_key] = {'text': '', 'chapter': current_chapter}
            if current_chapter:
                chapters[current_key] = current_chapter
            continue
        
        # Accumulate article text
        if current_key:
            articles[current_key]['text'] += line + '\n'
    
    # Clean up article text
    for key in articles:
        articles[key]['text'] = articles[key]['text'].strip()
    
    preamble = ' '.join(preamble_parts).strip()
    
    return {
        'preamble': preamble,
        'articles': articles,
        'chapters': chapters,
    }


def _build_placeholder_map(data: dict) -> dict:
    """Build a map of {placeholder_key: value} for substitution."""
    return {
        'osnivac_ime': data.get('osnivač_ime', ''),
        'osnivac_jmbg': data.get('osnivač_jmbg', ''),
        'osnivac_adresa': data.get('osnivač_adresa', ''),
        'osnivac_drzavljanstvo': data.get('osnivač_drzavljanstvo', ''),
        'drustvo_naziv': data.get('društvo_naziv', ''),
        'drustvo_naziv_skraceno': data.get('društvo_naziv_skraceno', ''),
        'drustvo_adresa': data.get('društvo_adresa', ''),
        'drustvo_kd': data.get('društvo_kd', ''),
        'drustvo_kapital': str(data.get('društvo_kapital', '0')),
        'kapital_slovima': data.get('kapital_slovima', ''),
        'direktor_ime': data.get('direktor_ime', ''),
        'direktor_jmbg': data.get('direktor_jmbg', ''),
        'datum_danas': data.get('datum_danas', ''),
        'skupstina_predsjednik': data.get('skupština_predsjednik', ''),
        'skupstina_zapisnicar': data.get('skupština_zapisničar', ''),
        'poslovodja_ime': data.get('poslovodja_ime', ''),
        'poslovodja_jmbg': data.get('poslovodja_jmbg', ''),
        'poslovodja_adresa': data.get('poslovodja_adresa', ''),
        'tip_djelatnosti': data.get('tip_djelatnosti', 'osnovna djelatnost'),
    }


def _substitute_placeholders(text: str, placeholder_map: dict) -> str:
    """Replace all {key} placeholders in text with their values."""
    result = text
    for key, value in placeholder_map.items():
        result = result.replace('{' + key + '}', str(value))
    return result


def _apply_dynamic_numbering(articles: dict, order: list, has_ostali: bool,
                              offset_start_key: str) -> list:
    """
    Apply dynamic article numbering.

    Args:
        articles: dict of {key: {text, chapter}} from wiki
        order: list of article keys in order
        has_ostali: whether there are additional activities
        offset_start_key: key from which numbering shifts by +1 when has_ostali

    Returns:
        list of {number, key, text, chapter, subchapter}
    """
    result = []
    offset = 0
    offset_applied = False
    
    for idx, key in enumerate(order):
        if key == 'ostale_djelatnosti':
            # This key is only present when has_ostali, skip otherwise
            continue
        
        if key not in articles:
            continue
        
        # Apply offset when we reach the offset start key and has_ostali
        if has_ostali and key == offset_start_key and not offset_applied:
            offset = 1
            offset_applied = True
        
        number = idx + 1 + offset
        
        article_text = articles[key]['text']
        chapter = articles[key].get('chapter', '')
        subchapter = STATUT_SUBCHAPTERS.get(key, '')
        
        result.append({
            'number': number,
            'key': key,
            'text': article_text,
            'chapter': chapter,
            'subchapter': subchapter,
        })
    
    return result


def _render_articles_to_html(articles: list, placeholder_map: dict) -> list:
    """Substitute placeholders in all articles and convert text to safe HTML."""
    for article in articles:
        text = article['text']
        text = _substitute_placeholders(text, placeholder_map)
        
        # Convert newlines to <br> tags for proper PDF rendering
        # But keep <ul>/<li> HTML intact (already from _generate_ostale_djelatnosti_article)
        if '<ul' not in text and '<li>' not in text:
            # Replace double newlines with paragraph breaks
            text = text.replace('\n\n', '</p><p>')
            # Replace single newlines with <br>
            text = text.replace('\n', '<br>\n')
            text = f'<p>{text}</p>'
        else:
            # Already has HTML, just handle newlines around it
            text = text.replace('\n', '<br>\n')
        
        article['content'] = text
    
    return articles


# ─── Dynamic List Article Generators ──────────────────────────────────────

def _generate_ostale_djelatnosti_article(data: dict, article_number: int) -> dict:
    """Generate the 'ostale djelatnosti' article dynamically from form data."""
    ostali_list = data.get('društvo_kd_ostali_list', [])
    if not ostali_list:
        return None
    
    lines = ['Pored pretežne djelatnosti, Društvo može obavljati i sljedeće djelatnosti:']
    lines.append('<ul class="djelatnosti">')
    for d in ostali_list:
        lines.append(f'<li>{d}</li>')
    lines.append('</ul>')
    
    return {
        'number': article_number,
        'key': 'ostale_djelatnosti',
        'text': '\n'.join(lines),
        'chapter': 'II DJELATNOST DRUŠTVA',
        'subchapter': '',
    }


def _generate_ostale_djelatnosti_odluka_article(data: dict, article_number: int) -> dict:
    """Generate 'ostale djelatnosti' for Odluka (inline after djelatnost)."""
    ostali_list = data.get('društvo_kd_ostali_list', [])
    if not ostali_list:
        return None
    
    lines = ['Društvo može obavljati i sljedeće djelatnosti:']
    for d in ostali_list:
        lines.append(f'  • {d}')
    
    # This is appended to the djelatnost article content, not a separate article
    return '\n'.join(lines)


def _generate_clanovi_drustva_html(data: dict) -> str:
    """Generate the founder list HTML for višečlani statut Član 5."""
    osnivaci = data.get('osnivači', [])
    if not osnivaci:
        return ''
    
    lines = ['(2) Članovi Društva su:']
    lines.append('<div class="list-item">')
    for i, o in enumerate(osnivaci, 1):
        lines.append(f'  {i}. {o["ime"]}, JMBG: {o["jmbg"]} — {o["procenat"]}% udjela<br>')
    lines.append('</div>')
    return '\n'.join(lines)


def _generate_udjeli_osnivaca_html(data: dict) -> str:
    """Generate the share list HTML for višečlani statut."""
    osnivaci = data.get('osnivači', [])
    kapital = int(data.get('društvo_kapital', 0))
    if not osnivaci:
        return ''
    
    lines = ['(1) Udjeli članova u osnovnom kapitalu iznose:']
    lines.append('<div class="list-item">')
    for i, o in enumerate(osnivaci, 1):
        iznos = int(kapital * o['procenat'] / 100)
        lines.append(f'  {i}. {o["ime"]} — {o["procenat"]}% ({iznos},00 EUR)<br>')
    lines.append('</div>')
    return '\n'.join(lines)


def _generate_direktori_list_html(data: dict) -> str:
    """Generate the director list HTML for višečlani documents."""
    direktori = data.get('direktori', [])
    if not direktori:
        return ''
    
    lines = ['<div class="list-item">']
    for i, d in enumerate(direktori, 1):
        lines.append(f'  {i}. {d["ime"]}, JMBG: {d["jmbg"]}<br>')
    lines.append('</div>')
    return '\n'.join(lines)


def _generate_osnivaci_list_html(data: dict) -> str:
    """Generate the founder list HTML for odluka višečlano Član 1."""
    osnivaci = data.get('osnivači', [])
    if not osnivaci:
        return ''
    
    lines = ['Ovom Odlukom, osnivači:']
    lines.append('<div class="founder-list">')
    for i, o in enumerate(osnivaci, 1):
        lines.append(f'<div class="founder-item">')
        lines.append(f'   {i}. {o["ime"]}, JMBG/PIB: {o["jmbg"]}, ')
        lines.append(f'   sa adresom: {o["adresa"]}, državljanstvo: {o["drzavljanstvo"]},')
        lines.append(f'   učešće u kapitalu: {o["procenat"]}%')
        lines.append(f'</div>')
    lines.append('</div>')
    lines.append('(u daljem tekstu: Osnivači), osnivaju društvo sa ograničenom odgovornošću (u daljem tekstu: Društvo).')
    return '\n'.join(lines)


def _generate_udjeli_osnivaca_odluka_html(data: dict) -> str:
    """Generate the founder shares list HTML for odluka višečlano Član 6."""
    osnivaci = data.get('osnivači', [])
    if not osnivaci:
        return ''
    
    lines = ['Osnivači stiču sljedeće udjele u Društvu:']
    lines.append('<div class="founder-list">')
    for i, o in enumerate(osnivaci, 1):
        lines.append(f'<div class="founder-item">')
        lines.append(f'   {i}. {o["ime"]} - {o["procenat"]}% udjela')
        lines.append(f'</div>')
    lines.append('</div>')
    return '\n'.join(lines)


def _apply_dynamic_content(articles: list, data: dict, doc_type: str) -> list:
    """
    Apply dynamic content to articles that have special keys.
    
    doc_type: 'statut-jednoclano', 'statut-viseclano', 'odluka-jednoclano', 'odluka-viseclano'
    """
    for article in articles:
        key = article.get('key', '')
        text = article.get('text', '')
        
        if key == 'osnivaci' and doc_type == 'odluka-viseclano':
            # Odluka višečlano: generate founder list (MUST be before generic checks)
            article['text'] = _generate_osnivaci_list_html(data)
        
        elif key == 'udjeli_osnivaca' and doc_type == 'odluka-viseclano':
            # Odluka višečlano: generate share list
            article['text'] = _generate_udjeli_osnivaca_odluka_html(data)
        
        elif key == 'direktori' and doc_type == 'odluka-viseclano':
            # Odluka višečlano: generate director list
            dir_html = _generate_direktori_list_html(data)
            if dir_html:
                article['text'] = 'Za direktore Društva imenuju se:\n' + dir_html
        
        elif key == 'clanovi_drustva':
            # Višečlani statut: insert founder list between (1) and (3)
            founder_html = _generate_clanovi_drustva_html(data)
            if founder_html:
                parts = text.split('(3) Članovi', 1)
                if len(parts) == 2:
                    article['text'] = parts[0] + founder_html + '\n(3) Članovi' + parts[1]
                else:
                    article['text'] = text + '\n' + founder_html
        
        elif key == 'udjeli_osnivaca':
            # Višečlani statut: insert share list
            shares_html = _generate_udjeli_osnivaca_html(data)
            if shares_html:
                article['text'] = shares_html + '\n' + text
        
        elif key in ('direktor_imenovanje',) and doc_type == 'statut-viseclano':
            # Višečlani statut: insert director list
            dir_html = _generate_direktori_list_html(data)
            if dir_html:
                parts = text.split('(3) Direktor se imenuje', 1)
                if len(parts) == 2:
                    article['text'] = parts[0] + '(2) Direktor(i) Društva su:\n' + dir_html + '\n(3) Direktor se imenuje' + parts[1]
        
        elif key == 'djelatnost' and doc_type.startswith('odluka'):
            # Odluka: append ostale djelatnosti if present
            extra = _generate_ostale_djelatnosti_odluka_article(data, 0)
            if extra:
                article['text'] = text + '<br>\n' + extra
    
    return articles


# ─── Public PDF Generation Functions ─────────────────────────────────────


def generate_odluka_pdf(data, session_id):
    """
    Generate Odluka o osnivanju PDF using wiki template.
    Falls back to old hardcoded template if wiki is unavailable.
    """
    data = _prepare_data(data)
    
    try:
        # Load and parse wiki template
        wiki_content = _load_wiki_template('templates', 'odluka-osnivanje-jednoclano')
        parsed = _parse_wiki_template(wiki_content)
        
        # Build placeholder map
        placeholder_map = _build_placeholder_map(data)
        
        # Get articles in order (no dynamic numbering for odluka)
        articles = []
        for idx, key in enumerate(ODLUKA_JEDNOCLANO_ORDER):
            if key not in parsed['articles']:
                continue
            articles.append({
                'number': idx + 1,
                'key': key,
                'text': parsed['articles'][key]['text'],
                'chapter': '',
                'subchapter': '',
            })
        
        # Apply dynamic content (ostale djelatnosti in djelatnost article)
        articles = _apply_dynamic_content(articles, data, 'odluka-jednoclano')
        
        # Render articles
        articles = _render_articles_to_html(articles, placeholder_map)
        
        # Build signatures
        datum = data.get('datum_danas', '')
        signatures = [
            {'label': 'Osnivač', 'name': data.get('osnivač_ime', ''), 'extra': f'Datum: {datum}'},
            {'label': 'Direktor', 'name': data.get('direktor_ime', ''), 'extra': f'Datum: {datum}'},
        ]
        
        # Render through wrapper template
        template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
        env = Environment(loader=FileSystemLoader(template_dir))
        
        template = env.get_template('odluka-wrapper.html')
        html_content = template.render(
            data=data,
            articles=articles,
            signatures=signatures,
            wiki_template='odluka-osnivanje-jednoclano.md',
        )
        
        output_filename = f"odluka-{session_id}.pdf"
        output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
        
        HTML(string=html_content).write_pdf(output_path)
        
        return output_path
        
    except FileNotFoundError as e:
        print(f"[WARN] Wiki template not available: {e}. Using hardcoded fallback.")
        return _generate_odluka_pdf_fallback(data, session_id)


def generate_statut_pdf(data, session_id):
    """
    Generate Statut DOO jednočlano PDF using wiki template.
    Falls back to old hardcoded template if wiki is unavailable.
    """
    data = _prepare_data(data)
    has_ostali = bool(data.get('društvo_kd_ostali_list'))
    
    try:
        # Load and parse wiki template
        wiki_content = _load_wiki_template('templates', 'statut-doo-jednoclano')
        parsed = _parse_wiki_template(wiki_content)
        
        # Build placeholder map
        placeholder_map = _build_placeholder_map(data)
        
        # Apply dynamic numbering
        articles = _apply_dynamic_numbering(
            parsed['articles'],
            STATUT_ARTICLE_ORDER,
            has_ostali,
            STATUT_OFFSET_START_KEY,
        )
        
        # Insert ostale_djelatnosti article if needed
        if has_ostali:
            ostali_article = _generate_ostale_djelatnosti_article(data, 7)
            if ostali_article:
                # Insert after pretezna_djelatnost (article 6), before dozvole
                insert_pos = 6  # Index of dozvole in the result (0-based)
                for i, a in enumerate(articles):
                    if a['key'] == 'dozvole':
                        insert_pos = i
                        break
                articles.insert(insert_pos, ostali_article)
        
        # Render article text with placeholders and HTML formatting
        articles = _render_articles_to_html(articles, placeholder_map)
        
        # Render preamble
        preamble = _substitute_placeholders(parsed['preamble'], placeholder_map)
        
        # Render through wrapper template
        template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
        env = Environment(loader=FileSystemLoader(template_dir))
        
        template = env.get_template('statut-wrapper.html')
        html_content = template.render(
            data=data,
            preamble=preamble,
            articles=articles,
            has_ostali=has_ostali,
        )
        
        output_filename = f"statut-{session_id}.pdf"
        output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
        
        HTML(string=html_content).write_pdf(output_path)
        
        return output_path
        
    except FileNotFoundError as e:
        # Fallback to old hardcoded template
        print(f"[WARN] Wiki template not available: {e}. Using hardcoded fallback.")
        return _generate_statut_pdf_fallback(data, session_id)


def _generate_statut_pdf_fallback(data, session_id):
    """Fallback: use old hardcoded template for jednočlani statut."""
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    template = env.get_template('statut-doo-jednočlano.html')
    html_content = template.render(data=data)
    
    output_filename = f"statut-{session_id}.pdf"
    output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
    
    HTML(string=html_content).write_pdf(output_path)
    
    return output_path


def _generate_odluka_pdf_fallback(data, session_id):
    """Fallback: use old hardcoded template for odluka jednočlano."""
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    template = env.get_template('odluka-osnivanje.html')
    html_content = template.render(data=data)
    
    output_filename = f"odluka-{session_id}.pdf"
    output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
    
    HTML(string=html_content).write_pdf(output_path)
    
    return output_path


def generate_odluka_pdf_višečlano(data, session_id):
    """
    Generate Odluka o osnivanju PDF for višečlano DOO using wiki template.
    """
    data = _prepare_data(data)
    
    try:
        wiki_content = _load_wiki_template('templates', 'odluka-osnivanje-viseclano')
        parsed = _parse_wiki_template(wiki_content)
        placeholder_map = _build_placeholder_map(data)
        
        articles = []
        for idx, key in enumerate(ODLUKA_VISECLANO_ORDER):
            if key not in parsed['articles']:
                continue
            articles.append({
                'number': idx + 1,
                'key': key,
                'text': parsed['articles'][key]['text'],
                'chapter': '',
                'subchapter': '',
            })
        
        articles = _apply_dynamic_content(articles, data, 'odluka-viseclano')
        articles = _render_articles_to_html(articles, placeholder_map)
        
        datum = data.get('datum_danas', '')
        direktori = data.get('direktori', [])
        prvi_direktor = direktori[0]['ime'] if direktori else ''
        signatures = [
            {'label': 'Predsjednik Skupštine', 'name': data.get('skupština_predsjednik', ''), 'extra': f'Datum: {datum}'},
            {'label': 'Direktor', 'name': prvi_direktor, 'extra': f'Datum: {datum}'},
        ]
        
        template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
        env = Environment(loader=FileSystemLoader(template_dir))
        
        template = env.get_template('odluka-wrapper.html')
        html_content = template.render(
            data=data,
            articles=articles,
            signatures=signatures,
            wiki_template='odluka-osnivanje-viseclano.md',
        )
        
        output_filename = f"odluka-višečlano-{session_id}.pdf"
        output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
        
        HTML(string=html_content).write_pdf(output_path)
        
        return output_path
        
    except FileNotFoundError as e:
        print(f"[WARN] Wiki template not available: {e}. Using hardcoded fallback.")
        return _generate_odluka_pdf_višečlano_fallback(data, session_id)


def _generate_odluka_pdf_višečlano_fallback(data, session_id):
    """Fallback: use old hardcoded template for odluka višečlano."""
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    template = env.get_template('odluka-osnivanje-višečlano.html')
    html_content = template.render(data=data)
    
    output_filename = f"odluka-višečlano-{session_id}.pdf"
    output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
    
    HTML(string=html_content).write_pdf(output_path)
    
    return output_path


def generate_statut_pdf_višečlano(data, session_id):
    """
    Generate Statut DOO višečlano PDF using wiki template.
    """
    data = _prepare_data(data)
    has_ostali = bool(data.get('društvo_kd_ostali_list'))
    
    try:
        wiki_content = _load_wiki_template('templates', 'statut-doo-viseclano')
        parsed = _parse_wiki_template(wiki_content)
        placeholder_map = _build_placeholder_map(data)
        
        # Apply dynamic numbering using višečlano order
        articles = _apply_dynamic_numbering(
            parsed['articles'],
            STATUT_VISECLANO_ORDER,
            has_ostali,
            STATUT_OFFSET_START_KEY,
        )
        
        # Override subchapters for višečlano
        for article in articles:
            if article['key'] in STATUT_VISECLANO_SUBCHAPTERS:
                article['subchapter'] = STATUT_VISECLANO_SUBCHAPTERS[article['key']]
        
        # Insert ostale_djelatnosti if needed
        if has_ostali:
            ostali_article = _generate_ostale_djelatnosti_article(data, 7)
            if ostali_article:
                for i, a in enumerate(articles):
                    if a['key'] == 'dozvole':
                        articles.insert(i, ostali_article)
                        break
        
        # Apply dynamic content (founder lists, director lists)
        articles = _apply_dynamic_content(articles, data, 'statut-viseclano')
        
        # Render articles
        articles = _render_articles_to_html(articles, placeholder_map)
        
        # Render preamble
        preamble = _substitute_placeholders(parsed['preamble'], placeholder_map)
        
        # Render through wrapper
        template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
        env = Environment(loader=FileSystemLoader(template_dir))
        
        template = env.get_template('statut-viseclano-wrapper.html')
        html_content = template.render(
            data=data,
            preamble=preamble,
            articles=articles,
            has_ostali=has_ostali,
        )
        
        output_filename = f"statut-višečlano-{session_id}.pdf"
        output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
        
        HTML(string=html_content).write_pdf(output_path)
        
        return output_path
        
    except FileNotFoundError as e:
        print(f"[WARN] Wiki template not available: {e}. Using hardcoded fallback.")
        return _generate_statut_pdf_višečlano_fallback(data, session_id)


def _generate_statut_pdf_višečlano_fallback(data, session_id):
    """Fallback: use old hardcoded template for višečlani statut."""
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    template = env.get_template('statut-doo-višečlano.html')
    html_content = template.render(data=data)
    
    output_filename = f"statut-višečlano-{session_id}.pdf"
    output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
    
    HTML(string=html_content).write_pdf(output_path)
    
    return output_path


# ─── Preduzetnik (TP) PDF Generation ─────────────────────────────────────

def generate_odluka_preduzetnik_pdf(data, session_id):
    """
    Generate Odluka o osnivanju preduzetnika PDF using wiki template.
    
    Unlike DOO, preduzetnik has no statut — only a single Odluka document.
    Poslovođa article is conditionally included.
    """
    data = _prepare_data(data)
    has_ostali = bool(data.get('društvo_kd_ostali_list'))
    has_poslovodja = bool(data.get('poslovodja_ime', '').strip())
    
    try:
        # Load and parse wiki template
        wiki_content = _load_wiki_template('templates', 'odluka-osnivanje-preduzetnik')
        parsed = _parse_wiki_template(wiki_content)
        
        # Build placeholder map
        placeholder_map = _build_placeholder_map(data)
        
        # Build main articles (without poslovodja)
        articles = []
        for idx, key in enumerate(ODLUKA_PREDUZETNIK_ORDER):
            if key not in parsed['articles']:
                continue
            articles.append({
                'number': idx + 1,
                'key': key,
                'text': parsed['articles'][key]['text'],
                'chapter': '',
                'subchapter': '',
            })
        
        # Apply dynamic content (ostale djelatnosti in djelatnost article)
        articles = _apply_dynamic_content(articles, data, 'odluka-preduzetnik')
        
        # Render article text with placeholders
        articles = _render_articles_to_html(articles, placeholder_map)
        
        # Build poslovodja article separately if needed
        articles_poslovodja = None
        if has_poslovodja:
            posl_key = 'poslovodja'
            if posl_key in parsed['articles']:
                posl_article = {
                    'number': len(articles) + 1,
                    'key': posl_key,
                    'text': parsed['articles'][posl_key]['text'],
                    'chapter': '',
                    'subchapter': '',
                }
                articles_poslovodja = _render_articles_to_html([posl_article], placeholder_map)
            else:
                # Fallback: generate inline poslovodja article
                posl_text = (
                    f"Za poslovođu Preduzetnika imenuje se: {data.get('poslovodja_ime', '')}, "
                    f"JMBG: {data.get('poslovodja_jmbg', '')}, "
                    f"sa adresom: {data.get('poslovodja_adresa', '')}. "
                    f"Poslovođa upravlja poslovima Preduzetnika na osnovu pisanog ovlašćenja "
                    f"i u skladu sa članom 91 Zakona o privrednim društvima."
                )
                posl_text = f'<p>{posl_text}</p>'
                articles_poslovodja = [{
                    'number': len(articles) + 1,
                    'key': 'poslovodja',
                    'content': posl_text,
                }]
        
        # Build signatures
        signatures = []
        if has_poslovodja:
            signatures.append({
                'label': 'Poslovođa',
                'name': data.get('poslovodja_ime', ''),
            })
        
        # Render through wrapper template
        template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
        env = Environment(loader=FileSystemLoader(template_dir))
        
        template = env.get_template('odluka-preduzetnik-wrapper.html')
        html_content = template.render(
            data=data,
            articles=articles,
            articles_poslovodja=articles_poslovodja,
            signatures=signatures,
            wiki_template='odluka-osnivanje-preduzetnik.md',
        )
        
        output_filename = f"odluka-preduzetnik-{session_id}.pdf"
        output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
        
        HTML(string=html_content).write_pdf(output_path)
        
        return output_path
        
    except FileNotFoundError as e:
        print(f"[ERROR] Wiki template not available: {e}")
        raise
