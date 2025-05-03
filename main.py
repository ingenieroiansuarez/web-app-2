import streamlit as st
from PIL import Image

with st.expander("Star camera"):
#start the camara
    camera_image = st.camera_input('Camera')

if camera_image:
# if the user has taken a picture
# show the image
    img  = Image.open(camera_image)
    #convert the image to grayscale
    gray_img = img.convert('L')
    #render the image
    st.image(gray_img)
