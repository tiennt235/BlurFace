import streamlit as st
import model

image = st.file_uploader("Choose a file to upload")

if image is not None:
    result = model.blur_face(image.name)
    st.image(result)
