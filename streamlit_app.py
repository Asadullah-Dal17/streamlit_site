import streamlit as st
import base64
from pathlib import Path


# Function to load image and convert it to base64
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


# Load the CSS file
def load_css():
    css = """
    @keyframes text-animation {
    0% {
        color: #2196F3;
    }

    50% {
        color: #4CAF50;
    }

    100% {
        color: #2196F3;
    }
    }




    img.profile-image {
    /* scrollbar-width: 23px; */
    /* border: #2196F3; */
    opacity: 50%;
    /* border-radius: 40%; */
    /* width: 100%;
    height: 100%; */
    /* object-fit: calc(%, 70%); */
    object-fit: cover;

    }

    img.profile-image:hover {
    transition: ease-in-out 0.5s;
    opacity: 100%;
    }


    body {
    /* font-family: 'Courier New', Courier, monospace; */
    background-color: #f5f5f5;
    color: #333;
    }

    h1 {
    background: linear-gradient(90deg, #ff8c00, #ff0080, #8000ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: animated-gradient 3s ease-in-out infinite;
    background-size: 200% 200%;
    }

    h2 {
    background: linear-gradient(90deg, #ff8c00, #ff0080, #8000ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: animated-gradient 3s ease-in-out infinite;
    background-size: 200% 200%;

    }

    h3 {
    background: linear-gradient(90deg, #ff8c00, #ff0080, #8000ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: animated-gradient 3s ease-in-out infinite;
    background-size: 200% 200%;

    }

    .container {

    font-size: 300px;
    /* font-family: 'Courier New', Courier, monospace; */
    font-weight: bolder;
    /* background: linear-gradient(90deg, #ff8c00, #ff0080, #8000ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: animated-gradient 3s ease-in-out infinite;
    background-size: 200% 200%; */
    }

    @keyframes animated-gradient {
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
    }



    .container .profile-image {
    width: 35%;
    height: 35%;
    border-radius: 10%;
    /* border-start-end-radius: 46%; */

    transition: width 0.3s ease, height 0.3s ease;
    }

    .container .profile-image:hover {
    width: 38%;
    height: 38%;
    }

    .container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 10px;
    }

    .profile-text {
    font-size: 200px;
    font-weight: bolder;
    /* color: #2196F3; */
    line-height: 1.5;
    text-align: justify;
    margin-top: 20px;
    }

    .social-icons {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
    gap: 30px;
    text-decoration: none;
    }

    .social-icons a:hover {
    transform: translateY(-10px);
    /* color: #C13584; */
    transition: transform 0.3s cubic-bezier(0.55, 0.055, 0.675, 0.19);
    }

    .social-icons {
    text-align: center;
    }

    .social-icons a {
    text-decoration: none;
    margin: 10px;
    }

    .social-icons a.facebook {
    color: #4267B2;
    }

    .social-icons a.twitter {
    color: #1DA1F2;
    }

    .social-icons a.linkedin {
    color: #0077B5;
    }

    .social-icons a.instagram {
    color: #C13584;
    }

    .social-icons a.github {
    color: #333;
    }

    .social-icons i {
    font-size: 3em;
    }

    .youtube_statics {
    /* display: flex; */
    font-size: 20px;
    justify-content: left;
    align-items: left;
    margin-top: 2px;
    gap: 50px;
    /* text-decoration: none; */
    }
    """
    return f"<style>{css}</style>"


# Load the HTML file
def load_html():
    html_code = """
    <div class="container">
        <div class="profile-text">
            <h1>Asadullah Dal</h1>
            <p class="profile-description">Asadullah Dal is an educator, YouTuber, and freelancer specializing in Computer
                Vision and Robotics. He
                founded AiPhile, a YouTube channel with over 3,000 subscribers, providing a comprehensive resource for
                learning and building computer vision projects. He also offers his expertise as a freelance computer vision
                developer, making him a sought-after professional in the field</p>
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
st.markdown(css, unsafe_allow_html=True)

# Load and inject HTML
html_file_path = Path("static\\template.html")
print(html_file_path)
html = load_html().format(image_base64=image_base64)
st.markdown(html, unsafe_allow_html=True)
