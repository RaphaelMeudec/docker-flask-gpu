"""
Defines the blueprint for the Classification
"""
from flask import Blueprint
from flask_restful import Api

from api.resources import ClassificationResource


CLASSIFICATION_BLUEPRINT = Blueprint('classification', __name__)
Api(CLASSIFICATION_BLUEPRINT).add_resource(
    ClassificationResource,
    '/classify'
)
