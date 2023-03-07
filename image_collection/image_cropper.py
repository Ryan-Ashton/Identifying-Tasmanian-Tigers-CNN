import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class ImageCropper:
    def __init__(self):
        self.width = None
        self.height = None
    
    def crop_images(self, source_path, output_path, left_crop=320, top_crop=50, right_crop=320, bottom_crop=50):
        """
        Crop images in a directory and save them in another directory.

        Args:
            source_path (str): The path to the directory containing the images to be cropped.
            output_path (str): The path to the directory where the cropped images should be saved.
            left_crop (int): The number of pixels to crop from the left side of the image. Default is 320.
            top_crop (int): The number of pixels to crop from the top of the image. Default is 50.
            right_crop (int): The number of pixels to crop from the right side of the image. Default is 320.
            bottom_crop (int): The number of pixels to crop from the bottom of the image. Default is 50.
        """
        counter = 0

        for filename in os.listdir(source_path):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                filepath = os.path.join(source_path, filename)

                img = Image.open(filepath)

                if counter == 0:
                    width, height = img.size
                    self.width = width
                    self.height = height

                cropped_img = img.crop((left_crop, top_crop, img.width-right_crop, img.height-bottom_crop))
                cropped_img = np.array(cropped_img)
                plt.imshow(cropped_img)
                plt.axis('off')
                image = Image.fromarray(cropped_img)
                print(image)
                image.save(f"{output_path}/{str(counter)}.jpeg")
                counter += 1