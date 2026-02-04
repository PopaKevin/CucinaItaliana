from flask import Blueprint, request, session, jsonify

carrello_bp = Blueprint('carrello_bp', __name__)

@carrello_bp.route('/carrello/add', methods=['POST'])
def add_carrello():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Non autenticato"})
    data = request.get_json()
    ricetta_id = data.get('ricetta_id')
    persone = data.get('persone', 1)
    vino_id = data.get('vino_id')  # opzionale

    if 'carrello' not in session:
        session['carrello'] = []
    session['carrello'].append({"ricetta_id": ricetta_id, "persone": persone, "vino_id": vino_id})
    return jsonify({"success": True, "carrello": session['carrello']})

if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    app.secret_key = "test_secret"

    # registra il blueprint
    app.register_blueprint(carrello_bp)

    # middleware temporaneo per simulare login
    @app.before_request
    def fake_login():
        from flask import session
        session['user_id'] = 1  # simula utente loggato

    # avvia Flask in modalità debug
    app.run(debug=True, port=5001)
