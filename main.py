import streamlit as st
from PIL import Image

st.subheader("Grayscale Image Converter")
## This is a simple image converter that converts an image to grayscale
# create a file uploader
uploaded_file = st.file_uploader("Choose an image file",
                                 type=['jpg', 'jpeg', 'png'])
#check if the user has uploaded a file
if uploaded_file:
    # open with PIL
    img = Image.open(uploaded_file)
    #convert to grayscale
    gray_img = img.convert('L')
    #display the image
    st.image(gray_img)

st.write("---")
with st.expander("Star camera"):
    st.write("Take a photo to convert to grayscale")
    camera_image = st.camera_input('Camera')

if camera_image:
# if the user has taken a picture
# show the image
    img  = Image.open(camera_image)
    #convert the image to grayscale
    gray_img = img.convert('L')
    #render the image
    st.image(gray_img)

 