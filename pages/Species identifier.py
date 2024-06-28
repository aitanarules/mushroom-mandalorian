import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

st.set_page_config(page_title="Identifier", page_icon="🔎")
st.sidebar.success("Choose a page")

st.title("Identify the mushroom!")
st.write("""This page will help you identify a mushroom species. For the moment, our application focuses on images with single object identification.
         Therefore, it may provide bad results when using images with multiple mushroom objects or not mushroom identified images.
         
         The species it is able to identy are the following:
         3 species:   
         * Agaricus augustus(edible)
         * Boletus pallidus(edible)
         * Daedaleopsis confragosa(toxic)
         """)

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
    try:
        shallow_cnn = load_model("./models/shallow_cnn.h5")
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        st.stop()

    # Make the prediction
    try:
        predictions = shallow_cnn.predict(img_array)
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        st.stop()

    # Ensure that predictions contain expected number of classes
    if predictions.shape[1] != 4:
        st.error("Unexpected number of predictions. Check the model and the input image.")
        st.stop()

    # Get the class with the highest probability
    predicted_class_index = np.argmax(predictions[0])

    # List of class names
    class_names = ["Agaricus augustus", "Boletus pallidus",  "Daedaleopsis confragosa"]


    # Get the predicted class name
    predicted_class_name = class_names[predicted_class_index]

    # Calculate probabilities
    result_html = f"""
    <div style="background-color: #ff5733; padding: 20px; border-radius: 10px; text-align: center;">
        <h2 style="color: #000000;">This mushroom is {predicted_class_name} with a {predictions[0][predicted_class_index]:.2f}% probability</h2>
    </div>
    """

    st.markdown(result_html, unsafe_allow_html=True)
