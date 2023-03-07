from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


class TestImageCropper:
    
    def __init__(self, left_crop=30, top_crop=50, right_crop=30, bottom_crop=50):
        """
        Initialize the ImageCropper object.
        
        Args:
        left_crop (int): The number of pixels to crop from the left side of the image. Default is 30.
        top_crop (int): The number of pixels to crop from the top of the image. Default is 50.
        right_crop (int): The number of pixels to crop from the right side of the image. Default is 30.
        bottom_crop (int): The number of pixels to crop from the bottom of the image. Default is 50.
        """
        self.left_crop = left_crop
        self.top_crop = top_crop
        self.right_crop = right_crop
        self.bottom_crop = bottom_crop
    
    def test_crop_image(self, image_path):
        """
        Crop an image using the specified crop amounts, 
        this is a useful method to use in a Jupyter Notebook before mass cropping a folder full of images.
        
        Args:
        image_path (str): The path to the image to be cropped.
        """
        # Open the image
        img = Image.open(image_path)
        original = np.array(img)

        fig, axs = plt.subplots(1, 2, figsize=(10, 5))

        axs[0].axis('off')
        axs[0].imshow(original)
        axs[0].set_title("original")

        # Crop the image
        cropped_img = img.crop((self.left_crop, self.top_crop, img.width-self.right_crop, img.height-self.bottom_crop))
        cropped_img = np.array(cropped_img)
        axs[1].imshow(cropped_img)
        axs[1].axis('off')
        image = Image.fromarray(cropped_img)
        print(image)
        axs[1].set_title("cropped")
        plt.show()

        
crop = TestImageCropper()
crop.test_crop_image(image_path=r"deep_learning_model_creation/kenji_tests/331087177_924274675652954_3411195455065388665_n.png")