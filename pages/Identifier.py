import streamlit as st
from PIL import Image

# Título de la aplicación
st.title("Subir y mostrar imágenes")

# Subir el archivo de imagen
uploaded_file = st.file_uploader("Elige una imagen...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Abre la imagen con PIL
    image = Image.open(uploaded_file)
    
    # Muestra la imagen
    st.image(image, caption='Imagen subida.', use_column_width=True)
    
    st.write("Formato de la imagen:", image.format)
    st.write("Tamaño de la imagen:", image.size)
    st.write("Modo de la imagen:", image.mode)
