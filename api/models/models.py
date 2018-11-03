from keras.applications import ResNet50
import tensorflow as tf


REFERENCE_GRAPH = tf.get_default_graph()
with REFERENCE_GRAPH.as_default():
    INITIALIZED_MODELS = {
        'resnet50': ResNet50(),
    }
