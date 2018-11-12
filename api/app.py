""" This module instanciates the Flask server and registers all routes """

from flask import Flask

from api.routes import CLASSIFICATION_BLUEPRINT


SERVER = Flask(__name__)

SERVER.register_blueprint(
    CLASSIFICATION_BLUEPRINT,
    url_prefix='/api'
)


if __name__ == '__main__':
    SERVER.run(host='0.0.0.0', port=8000, debug=True)
