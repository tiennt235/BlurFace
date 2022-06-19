import streamlit as st
import model
import numpy as np
from PIL import Image

uploaded_file = st.file_uploader("Choose a file to upload")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = image.convert('RGB')
    image = np.asarray(image)
    result = model.blur_face(image)
    st.image(result)
