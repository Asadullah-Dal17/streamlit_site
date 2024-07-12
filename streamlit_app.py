import streamlit as st
import base64
from pathlib import Path


def load_css():
    with open("style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# Function to load image and convert it to base64
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


# Load the CSS file
# def load_css():
#     css = """
#     return f"<style>{css}</style>"


# Load the HTML file
def load_html():
    html_code = """
    <div class="container">
        <div class="profile-text">
            <h1>Asadullah Dal</h1>
            <p class="profile-description">Hi there &#x1F44B;, I'm Asadullah, a passionate educator &#x1F468;&#x200D;&#x1F3EB; and freelance developer &#x1F468;&#x200D;&#x1F4BB; with expertise in Computer Vision &#x1F916;. I create educational videos on YouTube (AiPhile) to share my knowledge of computer vision and AI technologies. Get ready to embark on a journey of learning! &#x1F680;</p>
        </div>
        <img src="data:image/png;base64,{image_base64}" alt="Profile Image" class="profile-image">
    </div>
    """
    return html_code


# Path to the profile image (replace 'path/to/image.jpg' with the actual image path)
image_path = "images/my_image.png"
image_base64 = load_image(image_path)

# Load and inject CSS
css = load_css()

# Load and inject HTML
html = load_html().format(image_base64=image_base64)
st.markdown(html, unsafe_allow_html=True)
