from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User

users_bp = Blueprint("users", __name__)

@users_bp.route("", methods=["GET"])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify({"users": [u.to_dict() for u in users]}), 200


@users_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"user": user.to_dict()}), 200


@users_bp.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    current_user_id = int(get_jwt_identity())
    if user_id != current_user_id:
        return jsonify({"error": "Can only update your own profile"}), 403

    user = db.session.get(User, user_id)
    data = request.get_json()

    if data.get("email"):
        user.email = data["email"]
    if data.get("username"):
        user.username = data["username"]

    db.session.commit()
    return jsonify({"user": user.to_dict()}), 200


@users_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    current_user_id = int(get_jwt_identity())
    if user_id != current_user_id:
        return jsonify({"error": "Can only delete your own account"}), 403

    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200