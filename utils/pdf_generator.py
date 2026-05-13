import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from config import Config


def number_to_words(n, lang='sr'):
    """
    Convert number to words in Serbian.
    Handles numbers up to 999,999,999
    """
    ones = ['', 'jedan', 'dva', 'tri', 'četiri', 'pet', 'šest', 'sedam', 'osam', 'devet',
            'deset', 'jedanaest', 'dvanaest', 'trinaest', 'četrnaest', 'petnaest', 
            'šesnaest', 'sedamnaest', 'osamnaest', 'devetnaest']
    tens = ['', '', 'dvadeset', 'trideset', 'četrdeset', 'petdeset', 'šestdeset', 
            'sedamdeset', 'osamdeset', 'devetdeset']
    scales = ['', 'hiljada', 'miliona', 'milijardi']
    
    def _convert_chunk(n):
        if n < 20:
            return ones[n]
        elif n < 100:
            return tens[n // 10] + ('' if n % 10 == 0 else ones[n % 10])
        elif n < 1000:
            return ones[n // 100] + ('sto' if n % 100 == 0 else 'stotina' if n % 100 < 100 else ('sto ' + _convert_chunk(n % 100)))
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


def generate_odluka_pdf(data, session_id):
    """
    Generate Odluka o osnivanju PDF
    """
    # Add capital in words
    data['kapital_slovima'] = number_to_words(int(data['društvo_kapital']))
    
    # Setup Jinja2
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # Render template
    template = env.get_template('odluka-osnivanje.html')
    html_content = template.render(data=data)
    
    # Generate PDF
    output_filename = f"odluka-{session_id}.pdf"
    output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
    
    HTML(string=html_content).write_pdf(output_path)
    
    return output_path


def generate_statut_pdf(data, session_id):
    """
    Generate Statut DOO jednočlano PDF
    """
    # Add capital in words
    data['kapital_slovima'] = number_to_words(int(data['društvo_kapital']))
    
    # Setup Jinja2
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # Render template
    template = env.get_template('statut-doo-jednočlano.html')
    html_content = template.render(data=data)
    
    # Generate PDF
    output_filename = f"statut-{session_id}.pdf"
    output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
    
    HTML(string=html_content).write_pdf(output_path)
    
    return output_path


def generate_odluka_pdf_višečlano(data, session_id):
    """
    Generate Odluka o osnivanju PDF for višečlano DOO
    """
    # Add capital in words
    data['kapital_slovima'] = number_to_words(int(data['društvo_kapital']))
    
    # Setup Jinja2
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # Render template
    template = env.get_template('odluka-osnivanje-višečlano.html')
    html_content = template.render(data=data)
    
    # Generate PDF
    output_filename = f"odluka-višečlano-{session_id}.pdf"
    output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
    
    HTML(string=html_content).write_pdf(output_path)
    
    return output_path


def generate_statut_pdf_višečlano(data, session_id):
    """
    Generate Statut DOO višečlano PDF
    """
    # Add capital in words
    data['kapital_slovima'] = number_to_words(int(data['društvo_kapital']))
    
    # Setup Jinja2
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'pdf')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # Render template
    template = env.get_template('statut-doo-višečlano.html')
    html_content = template.render(data=data)
    
    # Generate PDF
    output_filename = f"statut-višečlano-{session_id}.pdf"
    output_path = os.path.join(Config.PDF_OUTPUT_DIR, output_filename)
    
    HTML(string=html_content).write_pdf(output_path)
    
    return output_path
