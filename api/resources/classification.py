"""
Define the REST verbs relative to the classification
"""
import io

from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
import numpy as np
from PIL import Image

from api.models import INITIALIZED_MODELS


class ClassificationResource(Resource):
    @staticmethod
    def get():

        image = Image.open(io.BytesIO(image))
        image = prepare_image(image, target=(224, 224))

        predictions = INITIALIZED_MODELS['resnet50'].predict(image)

        return 'prediction done!'


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
