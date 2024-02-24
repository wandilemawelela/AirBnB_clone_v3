#!/usr/bin/python3

"""
This module contains the routes for the status endpoint of the API.
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
    """
    status()

    Route that returns a JSON response with the status "OK".

    Returns:
        JSON: A JSON response with the status "OK".
    """
    return jsonify({"status": "OK"})
