import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image
import os
import cv2
import time
import streamlit.components.v1 as components

# Load the model
model = load_model('C:/Users/ryana/OneDrive/Documents/Python Scripts/tasmanian_tiger_vf/deep_learning_model_creation/saved_trained_model/assets/saved_trained_model.h5')

# Create a function to load an image

def load_image(img_path, img_shape=224):
    # Convert img_path to a string
    img_path = str(img_path)

    # Join the img_path to the base directory
    img_path = "C:/Users/ryana/OneDrive/Documents/Python Scripts/tasmanian_tiger_vf/deep_learning_model_creation/random_tests/received_756598882554027.jpeg"
    # img_path = os.path.join(base_dir, img_path)

    # Check if the file exists before reading it
    if not os.path.exists(img_path):
        st.write("Invalid image path!")
        return None

    # Load the image file as a tensor
    img = tf.io.read_file(img_path)
    
    # Decode image into tensor
    img = tf.io.decode_image(img, channels=3)

    
    # Resize the image
    img = tf.image.resize(img, [img_shape, img_shape])

    img = tf.reshape(img, shape=(1, 224, 224, 3))

    return img



# Create a function to predict the image
# Create a function to predict the image
def predict(img):
    img = load_image(img)
    if img is None:
        return None

    prediction = model.predict(img)
    return prediction


# Create a function to display the image
def display_image(img):
    img = Image.open(img)
    st.image(img, use_column_width=True)

# Create a function to display the result
def display_result(prediction):
    st.write(f"The probability of this being a Tasmania Tiger is: {str(round(prediction[0][0] * 100))}%")
    # if prediction == 0:
    #     st.write(str(prediction))
    #     st.write('The image is a Tasmanian Tiger')
    # else:
    #     st.write(str(prediction))
    #     st.write('The image is not a Tasmanian Tiger')

# Create a function to run the app
def run():
    # Add a title
    st.title('Tasmanian Tiger Image Classifier')

    # Add a sidebar
    st.sidebar.header('User Input Features')

    # Add a file uploader
    uploaded_file = st.sidebar.file_uploader('Upload an image of a Tasmanian Tiger', type=["png", "jpeg", "jpg"])
    
    # Convert the uploaded file to a PIL image
    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        # Convert the PIL image to a numpy array
        image_array = np.array(image)

        # Convert the numpy array to a Tensor
        image_tensor = tf.convert_to_tensor(image_array)

        # Add a button
        if st.sidebar.button('Classify'):
            # Display the image
            st.image(image)

            # Make a prediction
            prediction = predict(image_tensor)

            # Display the result
            display_result(prediction)

# Run the app
if __name__ == '__main__':
    run()




# conda create -n tastiger python=3.7

