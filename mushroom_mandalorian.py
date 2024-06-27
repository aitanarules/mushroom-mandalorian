import streamlit as st
from PIL import Image
import os

import json 
from streamlit_lottie import st_lottie 
  


# Page config
st.set_page_config(
    page_title="Fungi",
    page_icon="🍄",
)

# Title
st.write("# Welcome to Mushroom Mandalorian!")
st.sidebar.success("Choose a page")
st.subheader("This app will help you not to die while hunting mushrooms. ")

# Intial information
st.markdown("""Harnessing the power of Artificial Intelligence, Mushrooms Mandalorian is your ultimate tool 
            for identifying and classifying mushrooms based on their poisonousness. Whether you're a mycology 
            enthusiast, a forager, or just curious about mushrooms, our application provides a reliable, 
            user-friendly solution to keep you informed and safe.""")

# Some extra info


with st.container():
    st.write("---")
    left_column, right_column= st.columns((2))
    with left_column:
        st.header("Why Mushrooms Mandalorian is a must-have App?")
        st.write(
            """
            Every year, countless mushroom foragers and nature lovers encounter mushrooms that they cannot 
            identify. While some mushrooms are harmless or even highly nutritious, others can be extremely 
            poisonous, posing serious health risks. This is where Mushrooms Mandalorian steps in. 
            Our app leverages cutting-edge AI technology to provide accurate, instant identification of mushrooms, 
            ensuring that users can safely enjoy their outdoor adventures without the fear of accidental poisoning.
            """
        )
    with right_column:

        path = "./images/lottie_mushroom.json"
        with open(path,"r") as file: 
            url = json.load(file) 
        
    
        st.title("Adding Lottie Animation in Streamlit WebApp") 
        
        st_lottie(url, 
            reverse=True, 
            height=400, 
            width=400, 
            speed=1, 
            loop=True, 
            quality='high', 
            key='Car'
)




st.markdown("## Where to Find Mushrooms?")
st.markdown("""Mushrooms thrive in various environments, making them a fascinating and rewarding subject for foragers. 
            Here are some common places where you can find mushrooms:
            * Forests: Look around decaying wood, tree roots, and leaf litter.
            * Meadows and grasslands: Mushrooms often grow in grassy areas, especially after rainfall.
            * Gardens and yards: Check damp, shaded spots in your garden or backyard.
            * Near Water sources: Streams, rivers, and lakesides are prime spots for mushroom growth.""")

st.markdown("## Why Choose Mushrooms Mandalorian?")
st.markdown("""* Accuracy: Our AI model is trained on thousands of mushroom species to ensure precise identification.
            * Convenience: Easily identify mushrooms anywhere, anytime, with just a photo.
            * Safety: Make informed decisions and avoid poisonous mushrooms, protecting yourself and your loved ones.""")






# Testimonials:
# "Mushrooms Mandalorian has been a game-changer for my foraging trips. The AI is incredibly accurate and fast!" – Sarah T.
# "As a mushroom enthusiast, this app is a must-have. The interface is user-friendly, and the database is extensive." – John D.


# Get in Touch:
# For more information, support, or feedback, contact us at contact@mushroomsmandalorian.com. Follow us on social media for updates and tips!


# Función para cargar imágenes con verificación de existencia
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        st.error(f"Can't find the image right now :-) {image_path}")
        return None

# Crear dos columnas
col1, col2, col3 = st.columns(3)

# Edible mushrooms
with col1:
    st.markdown("## Edible mushrooms")
    st.markdown("Here we will show you some pictures of edible mushrooms. You can eat them without any danger.")
    images_yellow = [
        {"file": "images/edible_1.jpg", "caption": "Agaricus augustus"},
        {"file": "images/edible_2.jpg", "caption": "Mycena haematopus"},
        {"file": "images/edible_3.jpg", "caption": "Truffles"}
    ]

    selected_image_yellow = st.select_slider(
        "Edible mushrooms here:",
        options=[img['caption'] for img in images_yellow]
    )

    image_file_yellow = next(img['file'] for img in images_yellow if img['caption'] == selected_image_yellow)
    image_yellow = load_image(image_file_yellow)
    if image_yellow:
        st.image(image_yellow, caption=f"Edible mushroom: {selected_image_yellow}")

with col2:
    st.markdown("## Non edible mushrooms")
    st.markdown("Here we will show you some pictures of NON edible mushrooms.")
    images_blue = [
        {"file": "images/non_edible_1.jpg", "caption": "Fomitopsis mounceae"},
        {"file": "images/non_edible_2.jpg", "caption": "Hydnum repandum"},
        {"file": "images/non_edible_3.jpg", "caption": "Omphalotus olearius"}

    ]

    selected_image_blue = st.select_slider(
        "Non edible mushrooms here:",
        options=[img['caption'] for img in images_blue]
    )

    image_file_blue = next(img['file'] for img in images_blue if img['caption'] == selected_image_blue)
    image_blue = load_image(image_file_blue)
    if image_blue:
        st.image(image_blue, caption=f"Non edible mushroom: {selected_image_blue}")

with col3:
    st.markdown("## Toxic mushrooms")
    st.markdown("You may eat them and not die, but definetely you will feel bad after it.")
    images_green = [
        {"file": "images/toxic_1.jpg", "caption": "Amanita virosa"},
        {"file": "images/toxic_2.jpg", "caption": "Phlebia tremellosa"},
        {"file": "images/toxic_3.jpg", "caption": "Omphalotus illudens"},

    ]

    selected_image_green = st.select_slider(
        "Toxic mushrooms here:",
        options=[img['caption'] for img in images_green]
    )

    image_file_green = next(img['file'] for img in images_green if img['caption'] == selected_image_green)
    image_green = load_image(image_file_green)
    if image_green:
        st.image(image_green, caption=f"Toxic mushroom: {selected_image_green}")

