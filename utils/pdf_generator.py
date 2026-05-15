import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from config import Config
from utils.kd_reader import KDReader


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

    return data


def generate_odluka_pdf(data, session_id):
    """Generate Odluka o osnivanju PDF"""
    data = _prepare_data(data)
    
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    template = env.get_template('odluka-osnivanje.html')
    html_content = template.render(data=data)
    
    output_filename = f"odluka-{session_id}.pdf"
    output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
    
    HTML(string=html_content).write_pdf(output_path)
    
    return output_path


def generate_statut_pdf(data, session_id):
    """Generate Statut DOO jednočlano PDF"""
    data = _prepare_data(data)
    
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    template = env.get_template('statut-doo-jednočlano.html')
    html_content = template.render(data=data)
    
    output_filename = f"statut-{session_id}.pdf"
    output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
    
    HTML(string=html_content).write_pdf(output_path)
    
    return output_path


def generate_odluka_pdf_višečlano(data, session_id):
    """Generate Odluka o osnivanju PDF for višečlano DOO"""
    data = _prepare_data(data)
    
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    template = env.get_template('odluka-osnivanje-višečlano.html')
    html_content = template.render(data=data)
    
    output_filename = f"odluka-višečlano-{session_id}.pdf"
    output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
    
    HTML(string=html_content).write_pdf(output_path)
    
    return output_path


def generate_statut_pdf_višečlano(data, session_id):
    """Generate Statut DOO višečlano PDF"""
    data = _prepare_data(data)
    
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    template = env.get_template('statut-doo-višečlano.html')
    html_content = template.render(data=data)
    
    output_filename = f"statut-višečlano-{session_id}.pdf"
    output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
    
    HTML(string=html_content).write_pdf(output_path)
    
    return output_path
