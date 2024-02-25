#!/usr/bin/python3

"""
This module contains the routes for the status endpoint of the API.
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.user import User


@app_views.route('/status', methods=['GET'])
def status():
    """
    status()

    Route that returns a JSON response with the status "OK".

    Returns:
        JSON: A JSON response with the status "OK".
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    stats()

    Route that retrieves the number of each object by type.

    Returns:
        JSON: A JSON response with the counts of each object type.
    """

    classes = [Amenity, Place, User, City, Review, State]
    names = ['amenities', 'cities', 'places', 'reviews', 'states', 'users']
    numbers_obj = {}
    for i in range(len(classes)):
        numbers_obj[names[i]] = storage.count(classes[i])
    return jsonify(numbers_obj)


if __name__ == "__main__":
    pass
