#!/usr/bin/python3
"""
Defines the RESTful API for User Objects
"""

from flask import Flask, jsonify, request, abort
from models import storage
from api.v1.views import app_views
from models.user import User


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieve a specific user from his/her id"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """ Creates a User object. """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if 'email' not in data:
        abort(400, 'Missing email')
    if 'password' not in data:
        abort(400, 'Missing password')
    new_user = User(**data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """updating a user"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not JSON')
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieves the list of users"""
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """ delete a user"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404, 'error')
    storage.delete(user)
    storage.save()
    return jsonify({}), 200
