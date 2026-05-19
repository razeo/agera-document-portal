import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-prod')
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PDF_OUTPUT_DIR = os.path.join(BASE_DIR, 'generated_pdfs')
    
    # AGERA Wiki path — bundled in repo for deployment portability
    WIKI_PATH = os.environ.get('WIKI_PATH', os.path.join(BASE_DIR, 'wiki'))
    
    # Ensure PDF output dir exists
    os.makedirs(PDF_OUTPUT_DIR, exist_ok=True)
