import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from PIL import Image

from ImagePredictor import ImagePredictor

predictor = ImagePredictor('../deep_learning_model_creation/saved_trained_model/assets/saved_trained_model.h5')

# Create a function to run the app
def run():
    # Add a title
    st.title('Tasmanian Tiger Image Classifier')

    st.subheader("This application utilizes AI to calculate the probability of an image containing a Tasmanian Tiger.")

    # Background
    st.title("Background")

    st.write("The Tasmanian Tiger (Thylacine) has been considered extinct for over 50 years, however, many sightings of the animal have been reported since then.")

    st.write("To understand more about this topic please watch the following video:")

    st.video("https://www.youtube.com/watch?v=B9t0Buy4Ht4&t")

    # Methodology
    st.title("How the App Works")

    # Write a description of that App's function
    st.write("Users who have taken a picture of the Tasmanian Tiger but are uncertain about its identity can utilise the app to receive a probability score. The probability score corresponds to the likelihood of the image containing a Tasmanian Tiger, with a higher score indicating a greater likelihood.")

    # Add a header for the Image Classifier
    st.markdown('## Please upload your photo to see it contains a Tasmanian Tiger.')

    # Add a file uploader
    uploaded_file = st.file_uploader('Please note that no photos will be saved on our side', type=["png", "jpeg", "jpg"])
    
    # Convert the uploaded file to a PIL image
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = np.array(image)
        st.write("Please press the Classify button to see the result.")

        # Add a button
        if st.button('Classify'):
            # Display the image
            st.image(image)

            # Make a prediction
            prediction = predictor.predict(image)

            # Display the result
            predictor.display_result(prediction)
            predictor.result_description(prediction)


# Run the app
if __name__ == '__main__':
    run()




# conda create -n tastiger python=3.7

