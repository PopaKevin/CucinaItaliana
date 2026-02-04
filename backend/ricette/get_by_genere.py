from flask import Blueprint, jsonify
from db import get_db

genere_bp = Blueprint('genere_bp', __name__)

@genere_bp.route('/ricette/genere/<int:id_genere>', methods=['GET'])
def get_by_genere(id_genere):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT r.*
        FROM Ricetta r
        JOIN Ricetta_Genere rg ON r.ID_Ricetta = rg.ID_Ricetta
        WHERE rg.ID_Genere = %s
    """, (id_genere,))
    ricette = cursor.fetchall()
    return jsonify(ricette)
