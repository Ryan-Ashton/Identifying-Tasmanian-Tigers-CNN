import tensorflow as tf
import streamlit as st
from tensorflow.keras.models import load_model



class ImagePredictor:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def load_and_prep_image(self, img, img_shape=224):
        """
        Loads and pre-processes an image from a file.

        Parameters:
            img (str): The image input
            img_shape (int): The desired size of the image. Defaults to 224.

        Returns:
            Tensor: A pre-processed image tensor with shape (img_shape, img_shape, 3).

        """

        # Resize the image
        img = tf.image.resize(img, [img_shape, img_shape])
        img = tf.expand_dims(img, axis=0)
        return img 

    def predict(self, img):
        print("This is the shape before predict" + str(img.shape))
        img = self.load_and_prep_image(img)
        print("This is the shape for predict" + str(img.shape))
        prediction = self.model.predict(img)
        return prediction


    def display_result(self, prediction):
        return st.markdown(f"**The probability of this image containing a Tasmania Tiger is: {str(round(prediction[0][0] * 100))}%**")

    def result_description(self, prediction):
        if prediction[0][0] < 0.1:
            return st.write("At a probability score of < 10%, this image is unlikely to contain a Tasmanian Tiger.")
        elif prediction[0][0] < 0.2 and prediction[0][0] >= 0.1:
            return st.write("At a probability score of < 20%, this image is unlikely to contain a Tasmanian Tiger, but the picture appears to share some minor characteristics of a Tasmanian Tiger.")
        elif prediction[0][0] < 0.3 and prediction[0][0] >= 0.2:
            return st.write("At a probability score of < 30%, this image is unlikely to contain a Tasmanian Tiger, but the animal appears to have some characteristics of a Tasmanian Tiger.")
        elif prediction[0][0] < 0.4 and prediction[0][0] >= 0.3:
            return st.write("At a probability score of < 40%, this image is unlikely to contain a Tasmanian Tiger, or the picture is not clear enough for a proper classification.")
        elif prediction[0][0] < 0.5 and prediction[0][0] >= 0.4:
            return st.write("At a probability score of < 50%, this image is unlikely to contain a Tasmanian Tiger, or the picture is not clear enough for a proper classification. There could be a different animal in the picture that closely resembles a Tasmanian Tiger.")
        elif prediction[0][0] < 0.6 and prediction[0][0] >= 0.5:
            return st.write("At a probability score of < 60%, this image might be a Tasmanian Tiger, or a very good drawing of a Tasmanian Tiger.")
        elif prediction[0][0] < 0.7 and prediction[0][0] >= 0.6:
            return st.write("At a probability score of < 70%, this image might be a Tasmanian Tiger, or a very good drawing of a Tasmanian Tiger.")
        elif prediction[0][0] < 0.8 and prediction[0][0] >= 0.7:
            return st.write("You have an interesting picture here as this image might be a Tasmanian Tiger, or a very good drawing of a Tasmanian Tiger.")
        elif prediction[0][0] < 0.9 and prediction[0][0] >= 0.8:
            return st.write("This is a Tasmanian Tiger or a very good drawing of a Tasmanian Tiger.")
        elif prediction[0][0] < 1.0 and prediction[0][0] >= 0.9:
            return st.write("This is a Tasmanian Tiger or a very, very good drawing of a Tasmanian Tiger.")
        
        
        
