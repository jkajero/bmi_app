import streamlit as st
from PIL import Image

st.header("My BMI APP")

img = Image.open("health and wellness image.webp")
st.image(img)

weight = st.number_input("What is your weight(kg)",step = 0.1)
height = st.number_input("How tall are you (m)")

def bmi_calc(w,h):
    bmi = round(w/h**2,2)
    return bmi

def rating(b):
    if b > 25:
        st.write("You are at danger of being overweight")
    elif 18.4 < b < 25.1:
        st.write("You are doing well, keep it up")
    else:
        st.write("You are at danger of being underweight")
        
        
if st.button("Calculate"):
    score = bmi_calc(weight,height)
    st.write(score)
    rate = rating(score)