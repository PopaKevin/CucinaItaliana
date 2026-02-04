from flask import Blueprint, request, session, jsonify
from db import get_db

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Utente WHERE Username=%s AND Password=%s", (username, password))
    user = cursor.fetchone()
    if user:
        session['user_id'] = user['ID_Utente']
        session['username'] = user['Username']
        return jsonify({"success": True, "nome": user['Username']})
    return jsonify({"success": False})
