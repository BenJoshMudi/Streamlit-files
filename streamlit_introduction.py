import streamlit as st

# Title
st.title("THE BEGINNING OF DATA !!!")
st.header("NEW AGE")
st.subheader("WHERE ARE WE")
st.text("""
        In the beginning of data journey, I had a smooth ride with my learning progress for the fact that 
        i made use of a free udemy account to start my learning phase. At the same time,
        a friend supported me with time and more information about python code. 
        it is time to learn a new skill.

        
        
""")

st.header("THE END !!!")
st.success("success")
st.info("information")
st.warning("warning")

esp = ZeroDivisionError("Trying to divide by zero")
st.exception(esp)

# from PIL import Image

# img = Image.open("C:\Users\mudia\OneDrive\Desktop\RUTH.png")

# st.image(img, width=200)

import streamlit as st
from PIL import Image

# Open the image file using a raw string to avoid escape character issues
img = Image.open(r"C:\Users\mudia\OneDrive\Desktop\mudi (2).jpg")

img2 = Image.open(r"C:\Users\mudia\OneDrive\Desktop\Dashboard.png")

# Display the image in Streamlit with the specified width
st.image(img, width=300)
st.image(img2, width=1000)

if st.checkbox("open/close"):

    st.subheader("Make a wish !!!")

food = st.selectbox("What do you wish for: ", 
                    
                                    ['Fried Rice', 'A Private Jet', 'An Estate', 'Be A Citizen of your Favourite COuntry', 'Be a Billionaier'])

status = st.radio("Select Gender: ", ('M','F'))

if (status == 'M'):

    st.success("Male")

else:
    st.success("Female")


st.write("Congratulations: ", food)

food = st.multiselect("multiple wish: ", ['Fried Rice', 'A Private Jet', 'An Estate', 'Be A Citizen of your Favourite COuntry', 'Be a Billionaier'])

st.write("You Selected: ", len(food), 'wishes')

if st.button("About"):

    st.text("Welcome to Data Science !!!")

name = st.text_input("Enter your name: ", "Type here...  ")

if (st.button("Submit.")):
    
    result = name.title()

    st.success(result)

level = st.slider("Select the level: ", 1, 5)

st.text("selected: {}". format(level))


