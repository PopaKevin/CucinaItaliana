from flask import Blueprint, session, jsonify

view_bp = Blueprint('view_bp', __name__)

@view_bp.route('/carrello', methods=['GET'])
def view_carrello():
    carrello = session.get('carrello', [])
    return jsonify(carrello)
