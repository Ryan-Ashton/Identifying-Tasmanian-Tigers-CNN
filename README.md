# Identifying Tasmanian Tigers using Convolutional Neural Networks
## Introduction
This is a deep learning project in which I have developed a Convolutional Neural Network (CNN) to identify the probability of an image containing a Tasmanian Tiger or not. Tasmanian Tigers, also known as thylacines, are extinct carnivorous marsupials that once lived in the wilds of Tasmania, Australia. Despite being declared extinct in the 20th century, there have been many alleged sightings of Tasmanian Tigers, and identifying them from images can help further research and conservation efforts.

> This is a Non-For-Profit Project for the 1000s of people who go looking for the Tasmanian Tiger

The Deep Learning model has been deployed as a Web App at the following link: 

[Click Here To See App](https://tasmanian-tiger-image-classifier.streamlit.app/)

## App Interface
![alt text](/app/images/interface.jpg)


## Methodology

For this project, I collected a large dataset of images containing Tasmanian Tigers using a combination of web scraping and computer vision techniques. I used the Python CV (Computer Vision) library to extract screenshots from old footage of the Tasmanian Tiger and collected images from Google Images to build a comprehensive dataset.

To ensure the model could accurately identify Tasmanian Tigers from various types of images, I had to train it using both black and white as well as colored photos. This required careful preprocessing of the data to ensure consistency and minimize any potential bias.

## Experimentation
Throughout the development of this project, a number of experiments were conducted to optimize the performance of the CNN model, including:

Variations in transfer learning versus no transfer learning
- The use of different EfficientNet models
- Varying numbers of epochs
- Dropout versus no dropout
- Regularization versus no regularization
- Changes in learning rates
- Varying numbers of training images
- Varying data augmentation strategies

Each of these variations was tested to identify the combination of factors that produced the highest accuracy on both validation loss and validation accuracy metrics. Additionally, the model's ability to correctly classify random custom images that it had not seen before was also tested to ensure that it was able to generalize well.

After conducting all of these experiments and analyzing the results, I was able to identify the best combination of factors that achieved the highest levels of accuracy and generalization for the CNN model, including:

- The use of transfer learning
- Using the EfficientNetB0 model
- Training for a total of 11 epochs
- The use of L1 regularization with a factor of 0.001
- An Adam optimiser learning rate of 0.001
- A dataset of ~ 42,000 training images
- The use of data augmentation strategies including rotation, zooming, horizontal flipping, and width/height shift


