#!/usr/bin/python3

"""
This module contains the routes for the status endpoint of the API.
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity


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

    counts = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(counts)


if __name__ == "__main__":
    pass
