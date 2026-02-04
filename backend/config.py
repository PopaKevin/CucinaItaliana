import os

class Config:
    # Chiave segreta Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chiave-segreta-di-sviluppo'

    # Parametri database
    DB_HOST = 'mysql-3fe90f59-iisgalvanimi-1c9f.e.aivencloud.com'
    DB_PORT = 12798
    DB_USER = 'avnadmin'
    DB_PASSWORD = 'AVNS_9xFgbFLvCkBhZxys9sx'
    DB_NAME = 'CucinaItaliana'

    # Percorso assoluto al certificato SSL (cartella certs dentro backend)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # backend/
    SSL_CA_PATH = os.path.join(ROOT_DIR, 'certs', 'ca.pem')

    # Configurazione opzionale SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
