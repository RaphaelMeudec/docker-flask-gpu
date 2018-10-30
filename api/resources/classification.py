"""
Define the REST verbs relative to the classification
"""
from flask_restful import Resource

from keras.applications import ResNet50
from keras.applications.resnet50 import preprocess_input
from keras.preprocessing import image
import numpy as np
import tensorflow as tf

global model
model = ResNet50()
global graph
graph = tf.get_default_graph()

class ClassificationResource(Resource):
    @staticmethod
    def get():
        img = image.load_img('assets/cat.jpg', target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        with graph.as_default():
            results = model.predict(x)

        return 'prediction done!'
