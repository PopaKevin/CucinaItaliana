from flask import Blueprint, session, jsonify
from db import get_db

checkout_bp = Blueprint('checkout_bp', __name__)

@checkout_bp.route('/checkout', methods=['POST'])
def checkout():
    if 'user_id' not in session or 'carrello' not in session or not session['carrello']:
        return jsonify({"success": False, "message": "Carrello vuoto o utente non loggato"})

    conn = get_db()
    cursor = conn.cursor()

    # Crea ordine
    cursor.execute("INSERT INTO Ordine (ID_Utente) VALUES (%s)", (session['user_id'],))
    ordine_id = cursor.lastrowid

    # Aggiungi dettagli ordine
    for item in session['carrello']:
        cursor.execute("INSERT INTO Dettaglio_Ordine (ID_Ordine, ID_Ricetta, Persone, ID_Vino) VALUES (%s,%s,%s,%s)",
                       (ordine_id, item['ricetta_id'], item['persone'], item.get('vino_id')))
    conn.commit()

    session.pop('carrello')
    return jsonify({"success": True, "ordine_id": ordine_id})
