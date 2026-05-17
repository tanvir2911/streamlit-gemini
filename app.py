import streamlit as st

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

    if selected_difficulty:
        st.markdown(selected_difficulty)
    else:
        st.error("You must select a difficulty")

    button = st.button("Click the button to initiate AI")

    if button:
        if len(images)<0:
            st.error("Upload atleast 1 image")
        else:
            if selected_difficulty:
                st.error("Please choose a difficulty")
            # else:


