"""
Define the REST verbs relative to the classification
"""
from flask_restful import Resource

from keras.applications import ResNet50


class ClassificationResource(Resource):
    @staticmethod
    def get():
        return 'hello world!'
