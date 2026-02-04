import os
import pymysql
from config import Config

def get_db():
    """
    Restituisce una connessione al database MySQL con SSL
    """
    if not os.path.exists(Config.SSL_CA_PATH):
        raise FileNotFoundError(f"Certificato SSL non trovato: {Config.SSL_CA_PATH}")

    return pymysql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        port=Config.DB_PORT,
        ssl={'ca': Config.SSL_CA_PATH},
        cursorclass=pymysql.cursors.DictCursor
    )

# Test della connessione (solo se esegui direttamente db.py)
if __name__ == "__main__":
    try:
        conn = get_db()  # usa get_db() per coerenza con gli endpoint
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print("✅ Connessione al database riuscita!", result)
        conn.close()
    except Exception as e:
        print("❌ Errore di connessione:")
        print(e)
