import streamlit as st
import model
video = st.file_uploader("Choose a file to upload")

if video is not None:
    result_name = model.blur_face(video.name)
    st.video(result_name)
