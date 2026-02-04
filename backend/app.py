from flask import Flask
from flask_session import Session

# Configurazione
from config import Config

# Blueprint
from auth.login import login_bp
from auth.logout import logout_bp
from ricette.get_all import ricette_bp
from ricette.get_by_genere import genere_bp
from ricette.get_costo import costo_bp
from carrello.add import carrello_bp
from carrello.remove import remove_bp
from carrello.view import view_bp
from carrello.clear import clear_bp
from ordine.checkout import checkout_bp

# Crea app Flask
app = Flask(__name__)

# Configurazione chiave segreta e sessioni
app.secret_key = Config.SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Registrazione blueprint
app.register_blueprint(login_bp, url_prefix='/auth')
app.register_blueprint(logout_bp, url_prefix='/auth')
app.register_blueprint(ricette_bp, url_prefix='/ricette')
app.register_blueprint(genere_bp, url_prefix='/ricette')
app.register_blueprint(costo_bp, url_prefix='/ricette')
app.register_blueprint(carrello_bp, url_prefix='/carrello')
app.register_blueprint(remove_bp, url_prefix='/carrello')
app.register_blueprint(view_bp, url_prefix='/carrello')
app.register_blueprint(clear_bp, url_prefix='/carrello')
app.register_blueprint(checkout_bp, url_prefix='/ordine')

# Root route (opzionale)
@app.route('/')
def index():
    return "Benvenuto nella Cucina Italiana WebApp!"

# Avvio app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
