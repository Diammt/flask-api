# Here is all endpoints for our application
from .resources import *
from .start import app, api, reqparse, request, jsonify, swagger, handleError, g

# AUTHENTIFICATION

@app.route('/api')
def index():
    return jsonify({
      "hello": "world"
    }), 200


@app.route("/spec")
def spec():
    return jsonify(swagger(app))