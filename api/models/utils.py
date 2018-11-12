""" Utilities functions for the models such as imge preprocessing """

import numpy as np
from keras.applications import imagenet_utils
from keras.preprocessing.image import img_to_array


def prepare_image(image, target):
    """
    Apply preprocessing to a loaded image

    :param image: Pillow image
    :param target: Target size for the image
    :return: Preprocessed image as np.array
    """
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
