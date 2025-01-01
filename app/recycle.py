import tensorflow as tf
import numpy as np
from ultralytics import YOLO
import tensorflowjs as tfjs


def convert_model():
    #Test
    print("Converting model to tfjs start")
    model = YOLO("best.pt")
    model.export(format="tfjs")  
    print("Model converted to tfjs end")
    # Load the SavedModel
    model = tfjs.converters.load_keras_model('./best_web_model')

    # Save the Keras model
    model.save('best_keras.h5')
    input("Press Enter to exit...")

    # tensorflowjs_converter --input_format=keras best_keras.h5 best_tfjs

if __name__ == "__main__":
    convert_model()



