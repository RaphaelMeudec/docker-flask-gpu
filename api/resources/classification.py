"""
Define the REST verbs relative to the classification
"""
import io

from flask import jsonify
from flask_restful import Resource
from keras.applications import imagenet_utils
from keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image

from api.models.models import REFERENCE_GRAPH, INITIALIZED_MODELS


class ClassificationResource(Resource):
    @staticmethod
    def get():
        image = Image.open('assets/cat.jpg')
        image = prepare_image(image, target=(224, 224))

        with REFERENCE_GRAPH.as_default():
            predictions = INITIALIZED_MODELS['resnet50'].predict(image)

        results = imagenet_utils.decode_predictions(predictions)
        predictions = []

        # loop over the results and add them to the list of
        # returned predictions
        for (imagenetID, label, prob) in results[0]:
            r = {"label": label, "probability": float(prob)}
            predictions.append(r)


        return jsonify(predictions)


def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image
