import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

st.set_page_config(page_title="Identifier", page_icon="🔎")
st.title("Identify the mushroom!")
st.write("""This page will help you identify a mushroom. For the moment, our application focuses on images with single object identification.
         Therefore, it may provide bad results when using images with multiple mushroom objects or not mushroom identified images.""")

# Upload file
uploaded_file = st.file_uploader("Choose a picture...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open image using PIL
    image = Image.open(uploaded_file)
    
    st.write("### This is the image we're about to analyse:")

    # Show image
    st.image(image, caption='Uploaded image.', use_column_width=True)
    
    st.write("Image's format:", image.format)
    st.write("Image's size:", image.size)
    st.write("Image's mode:", image.mode)

    # Define image size
    img_height = 256
    img_width = 256

    # Convert the image to a format compatible with TensorFlow
    img = image.resize((img_height, img_width))  # Resize the image
    img_array = np.array(img)  # Convert the image to a numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to match the model input
    img_array = img_array / 255.0  # Normalize the image

    # Load the saved model
    shallow_cnn = load_model("./models/shallow_cnn.h5")

    # Make the prediction
    predictions = shallow_cnn.predict(img_array)

    # Get the class with the highest probability
    predicted_class_index = np.argmax(predictions[0])

    # List of class names
    class_names = ["Edible mushroom", "Edible sporocap", "Poisonous sporocap", "Poisonous mushroom"]

    # Get the predicted class name
    predicted_class_name = class_names[predicted_class_index]

    if 'Edible' in predicted_class_name:
        result_html = f"""
        <div style="background-color: #8dff33; padding: 20px; border-radius: 10px; text-align: center;">
            <h2 style="color: #000000;>"This mushroom is EDIBLE with an {(predictions[0]+predictions[1])*100}% probability</h2>
        </div>
        """
    else:
        result_html = f"""
        <div style="background-color: #ff5733; padding: 20px; border-radius: 10px; text-align: center;">
            <h2 style="color: #000000;>"This mushroom is NON EDIBLE with an {(predictions[2]+predictions[3])*100}% probability</h2>
        </div>
        """ 

    st.markdown(result_html, unsafe_allow_html=True)

    # Display the result
    # st.write(f"The image is predicted as: {predicted_class_name}")
    # st.write(f"Probabilities: {predictions[0]}")
