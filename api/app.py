from flask import Flask
from keras.applications import ResNet50

from routes import CLASSIFICATION_BLUEPRINT


server = Flask(__name__)

server.register_blueprint(
    CLASSIFICATION_BLUEPRINT,
    url_prefix='/api'
)


global model
model = ResNet50()

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8000, debug=True)
