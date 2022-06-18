import streamlit as st
import model

subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

video = st.file_uploader("Choose a file to upload")

if video is not None:
    result_name = model.blur_face(video.name)
    st.video(result_name)
