import streamlit as st
import base64
from pathlib import Path


# Function to load image and convert it to base64
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


# Load the CSS file
def load_css(file_name):
    with open(file_name) as f:
        return f"<style>{f.read()}</style>"


# Load the HTML file
def load_html(file_name):
    with open(file_name) as f:
        return f.read()


# Path to the profile image (replace 'path/to/image.jpg' with the actual image path)
image_path = "images/my_image.png"
image_base64 = load_image(image_path)

# Load and inject CSS
css_file_path = Path("static\style.css")
css = load_css(css_file_path)
st.markdown(css, unsafe_allow_html=True)

# Load and inject HTML
html_file_path = Path("static\\template.html")
print(html_file_path)
html = load_html(html_file_path).format(image_base64=image_base64)
st.markdown(html, unsafe_allow_html=True)
