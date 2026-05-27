import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


images = st.file_uploader(
    "Upload the photos of your notes",
    type=["jpg","jpeg","png"],
    accept_multiple_files=True
)

if images:
    pil_images = []

    for img in images:
        pil_images.append(Image.open(img))

    prompt = """Summarize the picture in note format at max 100 words, 
    make sure to add necessary markdown to differentiate different sections"""
    response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[pil_images, prompt]
        )
    st.text(response.text)