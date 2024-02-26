#!/usr/bin/python3
"""
Defines the RESTful API actions for City objects
"""

from flask import Flask, jsonify, request, abort
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City
from models import storage

@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_cities(state_id):
   """Getting the city"""
   ## check state_ids in the storage
   stat_id = storage.get(State, state_id)
   if stat_id is None:
       abort(404)
   else:
       pass
