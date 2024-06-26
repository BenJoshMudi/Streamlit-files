# import the streamlit library

import streamlit as st

# give a title to our app

st.title("Welcome To BMI CALCULATOR")

weight = st.number_input("Enter your weight (in kgs)")

height = st.number_input("Enter your Height ")

status = st.radio("Select your height formate: ", ('cms','meters', 'feet' ))

if (status == 'cms'):

    height = st.number_input("Centimeters")
    
    try:
        bmi = weight / ((height/100) * 2)

    except:
        st.text("Enter some value of height")

elif (status == 'meters'):

    height = st.number_input("Meters")

    try:

        bmi = weight / (height ** 2)

    except:
        
        st.text("Enter some value of height")

else:

    height = st.number_input("Feet")
    # 1 meter = 3.28
    try:
        
        bmi = weight / (((height * 1.38) **2))

    except:

        st.text("Enter some value of height")

    
if (st.button("Calculate BMI")):
     # print the BMI index
    
    st.text("Your BMI index is {}.".format(bmi))

    # Give the interpretion of BMI Index
    if (bmi <16):
        st.error("You are extremely underweight")

    elif (bmi >= 16 and bmi < 18.5):

        st.warning("You are underweight")

    elif (bmi >=18.5 and bmi < 25):

        st.success("Healthy")

    elif (bmi>25 and bmi <30):
        
        st.warning("Overweight")

    elif (bmi >= 30):

        st.error("Extremely Overweight")





        
