import streamlit as st
import model
import numpy as np
from PIL import Image

from streamlit_option_menu import option_menu

# 1. as sidebar menu
st.title('Blur Face Web App')
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'About us'], 
        icons=['house','info'], menu_icon="cast", default_index=0)
    selected

if selected=='Home':

  uploaded_file = st.file_uploader("Choose a image to upload")

  if uploaded_file is not None:
      image = Image.open(uploaded_file)
      image = image.convert('RGB')
      image = np.asarray(image)
      result = model.blur_face(image)
      st.image(result)

if selected=='About us':

  st.title("About us")
  st.subheader("1. Nguyen Tran Tien")
  st.subheader("2. Luong Trieu Vy")
  st.subheader("3. Nguyen Quoc Huy Hoang")
  st.subheader("4. Danh Vo Hong Phuc")
  st.subheader("5. Le Nguyen Khanh Nam")
