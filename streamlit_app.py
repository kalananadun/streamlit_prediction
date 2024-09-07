import streamlit as st
from predict_page import show_predict
from explore_page import show_explore_page
def add_bg_from_url():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://media.post.rvohealth.io/wp-content/uploads/2020/09/doctor_glucosmeter_patient_hand-1200x628-FACEBOOK-1200x628.jpg');
            background-size: cover;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# Call the function to add the background
add_bg_from_url()

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict()
else:
    show_explore_page()
