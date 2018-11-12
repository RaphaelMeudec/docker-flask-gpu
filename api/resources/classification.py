"""
Define the REST verbs relative to the classification
"""
from flask import jsonify
from flask_restful import Resource
from keras.applications import imagenet_utils
from PIL import Image

from api.models.models import REFERENCE_GRAPH, INITIALIZED_MODELS
from api.models.utils import prepare_image

class ClassificationResource(Resource):
    @staticmethod
    def get():
        image = Image.open('assets/cat.jpg')
        image = prepare_image(image, target=(224, 224))

        with REFERENCE_GRAPH.as_default():
            predictions = INITIALIZED_MODELS['resnet50'].predict(image)

        results = imagenet_utils.decode_predictions(predictions)[0]
        predictions = {
            {
                "label": class_label,
                "probability": float(class_probability),
            } for (_, class_label, class_probability) in results
        }

        return jsonify(predictions)
