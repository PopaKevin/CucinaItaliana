from flask import Blueprint, jsonify
from db import get_db

costo_bp = Blueprint('costo_bp', __name__)

@costo_bp.route('/ricette/costo/<int:id_ricetta>', methods=['GET'])
def get_costo(id_ricetta):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.ID_Ricetta, SUM(ri.Quantita * i.PrezzoUnitario) AS costo
        FROM Ricetta_Ingrediente ri
        JOIN Ingrediente i ON ri.ID_Ingrediente = i.ID_Ingrediente
        WHERE ri.ID_Ricetta = %s
        GROUP BY r.ID_Ricetta
    """, (id_ricetta,))
    costo = cursor.fetchone()
    return jsonify({"costo_per_persona": float(costo[0]) if costo else 0})
