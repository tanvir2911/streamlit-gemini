import streamlit as st
from api_calling import note_generator
from PIL import Image

st.title("Note summary and quiz generator")
st.markdown("Upload upto 3 images to generate note summary and quizzes")
st.divider()

with st.sidebar:
    st.header("Controlls")
    images = st.file_uploader(
        "Upload the photos of your notes",
        type=["jpg","jpeg","png"],
        accept_multiple_files=True
    )

    # images
    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            col = st.columns(len(images))
            st.subheader("Uploaded Images")
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)

    # difficulty
    selected_difficulty = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy", "Medium", "Hard"),
        index=None
    )

    pressed = st.button("Click the button to initiate AI")

if pressed:
    if not images:
        st.error("You must upload an image")
    if not selected_difficulty:
        st.error("You must choose a difficulty")
    
    if images and selected_difficulty:
        # note
        with st.container(border=True):
            st.subheader("Your Note")
            st.text(note_generator(images))

        # Audio Transcript
        with st.container(border=True):
            st.subheader("Audio Transcription")
            st.text("Audion scrpt wil be sonw")

        # quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_difficulty})")
            st.text("Quiz scrpt wil be sonw")



