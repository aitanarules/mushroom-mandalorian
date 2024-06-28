import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

st.set_page_config(page_title="Identifier", page_icon="🔎")
st.title("Identify the mushroom!")
st.write("""This page will help you identify a mushroom. For the moment, our application focuses on images with single object identification.
         Therefore, it may provide bad results when using images with multiple mushroom objects or not mushroom identifed images.""")




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





    # Define el tamaño de la imagen
    img_height = 256
    img_width = 256

    # Cargar y preprocesar la imagen
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(img_height, img_width))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Cargar el modelo guardado
    shallow_cnn = load_model("./models/shallow_cnn.h5")

    # Hacer la predicción
    predictions = shallow_cnn.predict(img_array)

    # Obtener la clase con la mayor probabilidad
    predicted_class_index = np.argmax(predictions[0])

    # Lista de nombres de las clases
    class_names = ["edible_mushroom", "edible_sporocap", "poisonous_sporocap", "posinous_mushroom" ]

    # Obtener el nombre de la clase predicha
    predicted_class_name = class_names[predicted_class_index]

    # Imprimir el resultado
    print(f"La imagen es predicha como: {predicted_class_name}")

    # Imprimir las probabilidades
    print(f"Probabilidades: {predictions[0]}")

