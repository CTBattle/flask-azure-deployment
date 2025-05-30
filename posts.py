from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Post

posts_bp = Blueprint('posts', __name__)

# Create a post (JWT protected)
@posts_bp.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    user_id = get_jwt_identity()

    if not title or not content:
        return jsonify({'error': 'Title and content required'}), 400

    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    return jsonify({'message': 'Post created', 'id': new_post.id}), 201


# List all posts (public)
@posts_bp.route('/posts', methods=['GET'])
def list_posts():
    posts = Post.query.all()
    return jsonify([{
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author_id': post.user_id
    } for post in posts])


# Get a single post by ID (public)
@posts_bp.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify({
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author_id': post.user_id
    })


# Update a post (JWT protected, only if owner)
@posts_bp.route('/posts/<int:post_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    current_user_id = get_jwt_identity()

    if post.user_id != current_user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    db.session.commit()

    return jsonify({'message': 'Post updated successfully'})


# Delete a post (JWT protected, only if owner)
@posts_bp.route('/posts/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    current_user_id = get_jwt_identity()

    if post.user_id != current_user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted successfully'})
