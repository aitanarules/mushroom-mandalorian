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
                
        st_lottie(url, 
            reverse=True, 
            height=400, 
            width=400, 
            speed=1, 
            loop=True, 
            quality='high', 
            key='mushroom'
)


with st.container():
    left_column, right_column= st.columns((2))
    with right_column:
        st.header("Where to find mushrooms?")
        st.write(
            """
            Mushrooms thrive in various environments, making them a fascinating and rewarding subject for foragers. 
            Here are some common places where you can find mushrooms:
            * Forests: Look around decaying wood, tree roots, and leaf litter.
            * Meadows and grasslands: Mushrooms often grow in grassy areas, especially after rainfall.
            * Gardens and yards: Check damp, shaded spots in your garden or backyard.
            * Near Water sources: Streams, rivers, and lakesides are prime spots for mushroom growth.
            """
        )
    with left_column:

        path = "./images/lottie_finding.json"
        with open(path,"r") as file: 
            url = json.load(file) 
                
        st_lottie(url, 
            reverse=True, 
            height=300, 
            width=300, 
            speed=1, 
            loop=True, 
            quality='high', 
            key='find'
)
        


with st.container():
    left_column, right_column= st.columns((2))
    with left_column:
        st.header("Why Choose Mushrooms Mandalorian?")
        st.write(
            """
            * Accuracy: Our AI model is trained on thousands of mushroom species to ensure precise identification.
            * Convenience: Easily identify mushrooms anywhere, anytime, with just a photo.
            * Safety: Make informed decisions and avoid poisonous mushrooms, protecting yourself and your loved ones.
            """
        )
    with right_column:

        path = "./images/lottie_star.json"
        with open(path,"r") as file: 
            url = json.load(file) 
                
        st_lottie(url, 
            reverse=True, 
            height=400, 
            width=400, 
            speed=1, 
            loop=True, 
            quality='high', 
            key='star'
)

with st.container():
    st.title("Testimonials")
    st.write('"Mushrooms Mandalorian has been a game-changer for my foraging trips. The AI is incredibly accurate and fast!" – Sarah T. ')
    st.write('"As a mushroom enthusiast, this app is a must-have. The interface is user-friendly, and the database is extensive." – John D.')



# Function to upload images
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        st.error(f"Can't find the image right now :-) {image_path}")
        return None

# Create 3 columns
col1, col2, col3 = st.columns(3)

# Edible mushrooms
with col1:
    st.markdown("## Edible mushrooms")
    st.markdown("Here we will show you some pictures of edible mushrooms. You can eat them without any danger.")
    images_edible = [
        {"file": "images/edible_1.jpg", "caption": "Agaricus augustus"},
        {"file": "images/edible_2.jpg", "caption": "Mycena haematopus"},
        {"file": "images/edible_3.jpg", "caption": "Truffles"}
    ]

    selected_image_edible = st.select_slider(
        "Edible mushrooms here:",
        options=[img['caption'] for img in images_edible]
    )

    image_file_edible = next(img['file'] for img in images_edible if img['caption'] == selected_image_edible)
    image_edible = load_image(image_file_edible)
    if image_edible:
        st.image(image_edible, caption=f"Edible mushroom: {selected_image_edible}")

with col2:
    st.markdown("## Non edible mushrooms")
    st.markdown("Here we will show you some pictures of NON edible mushrooms.")
    images_non_edible = [
        {"file": "images/non_edible_1.jpg", "caption": "Fomitopsis mounceae"},
        {"file": "images/non_edible_2.jpg", "caption": "Hydnum repandum"},
        {"file": "images/non_edible_3.jpg", "caption": "Omphalotus olearius"}

    ]

    selected_image_non_edible = st.select_slider(
        "Non edible mushrooms here:",
        options=[img['caption'] for img in images_non_edible]
    )

    image_file_non_edible = next(img['file'] for img in images_non_edible if img['caption'] == selected_image_non_edible)
    image_non_edible = load_image(image_file_non_edible)
    if image_non_edible:
        st.image(image_non_edible, caption=f"Non edible mushroom: {selected_image_non_edible}")

with col3:
    st.markdown("## Toxic mushrooms")
    st.markdown("You may eat them and not die, but definetely you will feel bad after it.")
    images_toxic = [
        {"file": "images/toxic_1.jpg", "caption": "Amanita augusta"},
        {"file": "images/toxic_2.jpg", "caption": "Phlebia tremellosa"},
        {"file": "images/toxic_3.jpg", "caption": "Omphalotus illudens"},

    ]

    selected_image_toxic = st.select_slider(
        "Toxic mushrooms here:",
        options=[img['caption'] for img in images_toxic]
    )

    image_file_toxic = next(img['file'] for img in images_toxic if img['caption'] == selected_image_toxic)
    image_toxic = load_image(image_file_toxic)
    if image_toxic:
        st.image(image_toxic, caption=f"Toxic mushroom: {selected_image_toxic}")



# Get in Touch:
# For more information, support, or feedback, contact us at contact@mushroomsmandalorian.com. Follow us on social media for updates and tips!


# with st.container():
#     st.write("---")
#     st.header("Ponte en contacto con nosotros!")
#     st.write("##")
#     contact_form = f"""
#     <form action="https://formsubmit.co/{email_address}" method="POST">
#         <input type="hidden" name="_captcha" value="false">
#         <input type="text" name="name" placeholder="Tu nombre" required>
#         <input type="email" name="email" placeholder="Tu email" required>
#         <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
#         <button type="submit">Enviar</button>
#     </form>
#     """
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.markdown(contact_form, unsafe_allow_html=True)
#     with right_column:
#         st.empty()
