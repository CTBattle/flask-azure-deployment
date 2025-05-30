from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User, Post

users_bp = Blueprint('users', __name__)

# Get your own profile
@users_bp.route('/me', methods=['GET'])
@jwt_required()
def get_my_profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)

    return jsonify({
        'id': user.id,
        'username': user.username
    })


# Get another user's profile by ID
@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = User.query.get_or_404(user_id)

    return jsonify({
        'id': user.id,
        'username': user.username
    })


# Get all posts by a user
@users_bp.route('/users/<int:user_id>/posts', methods=['GET'])
def get_user_posts(user_id):
    posts = Post.query.filter_by(user_id=user_id).all()

    return jsonify([{
        'id': post.id,
        'title': post.title,
        'content': post.content
    } for post in posts])
