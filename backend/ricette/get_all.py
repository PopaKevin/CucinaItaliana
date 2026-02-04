from flask import Blueprint, jsonify
from db import get_db

ricette_bp = Blueprint('ricette_bp', __name__)

@ricette_bp.route('/ricette', methods=['GET'])
def get_all_ricette():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Ricetta")
    ricette = cursor.fetchall()
    return jsonify(ricette)
