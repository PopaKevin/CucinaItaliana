from flask import Blueprint, session, jsonify

logout_bp = Blueprint('logout_bp', __name__)

@logout_bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return jsonify({"success": True})
