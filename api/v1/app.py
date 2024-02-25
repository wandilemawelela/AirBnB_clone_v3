#!/usr/bin/python3

"""
This module serves as the entry point for the API application.
"""

<<<<<<< HEAD
from urllib.parse import quote as url_quote
from flask import Flask
from models import storage
=======
from models import storage
from flask import Flask, jsonify
>>>>>>> origin/master
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)

# Enable pretty-printing of JSON responses
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
    teardown(exception)

    Function to be executed when the application context is torn down.
    It closes the database connection.

    Args:
        exception: An exception object, if any, that triggered the teardown.

    Returns:
        None
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors by returning a JSON-formatted response.
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
