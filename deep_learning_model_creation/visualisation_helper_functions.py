import matplotlib.pyplot as plt
import tensorflow as tf


def load_and_prep_image(filename, img_shape=224):
    """
    Loads and pre-processes an image from a file.

    Parameters:
        filename (str): The path to the image file.
        img_shape (int): The desired size of the image. Defaults to 224.
        
    Returns:
        Tensor: A pre-processed image tensor with shape (img_shape, img_shape, 3).
        
    """

    # Read in the image
    img = tf.io.read_file(filename)

    # Decode image into tensor
    img = tf.io.decode_image(img, channels=3)

    # Resize the image
    img = tf.image.resize(img, [img_shape, img_shape])

    return img 


def pred_and_plot(model, filename, class_names=['not_tasmanian_tiger', 'tasmanian_tiger']):
    
  # Import the target image and preprocess it
    img = load_and_prep_image(filename)
    
  # Make a prediction
    pred = model.predict(tf.expand_dims(img, axis=0))
    pred_text = "The probability of this being a Tasmania Tiger is: " + str(round(pred[0][0] * 100)) + "%"

    plt.imshow(img/255)
    plt.title(f"Prediction: {pred_text}")
    plt.axis(False)


def plot_history(history):
    
    """
    Plots the loss and accuracy metrics of a Keras model during training.

    Parameters:
        history (keras.callbacks.History): The `history` object returned by the `fit()` method of a Keras model.

    Returns:
        None

    """
    
    # Extract the loss and accuracy values for plotting
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    # Create a new figure for plotting
    plt.figure(figsize=(12, 6))

    # Plot the training and validation loss
    plt.subplot(1, 2, 1)
    plt.plot(loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')
    plt.title('Loss over Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    # Plot the training and validation accuracy
    plt.subplot(1, 2, 2)
    plt.plot(acc, label='Training Accuracy')
    plt.plot(val_acc, label='Validation Accuracy')
    plt.title('Accuracy over Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()

    # Display the plot
    plt.show()