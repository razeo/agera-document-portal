import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-prod')
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PDF_OUTPUT_DIR = os.path.join(BASE_DIR, 'generated_pdfs')
    
    # AGERA Wiki path
    WIKI_PATH = os.path.join(os.path.expanduser('~'), 'agera-knowledge', 'wiki')
    
    # Ensure PDF output dir exists
    os.makedirs(PDF_OUTPUT_DIR, exist_ok=True)