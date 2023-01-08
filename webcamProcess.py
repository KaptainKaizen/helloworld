import streamlit as st
import cv2 
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None: 
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    st.write(type(cv2_img))

    st.write(cv2_img.shape)

st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green')
)

st.write('Your favorite color is ', option)