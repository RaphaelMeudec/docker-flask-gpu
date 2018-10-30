"""
Define the REST verbs relative to the classification
"""
from flask_restful import Resource


class ClassificationResource(Resource):
    @staticmethod
    def get():
        return 'hello world!'
