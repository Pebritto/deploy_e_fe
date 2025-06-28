from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result = AuthService.register_user(data)
    return jsonify(result), 201 if result['success'] else 400

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result = AuthService.authenticate_user(data)
    return jsonify(result)