import streamlit as st
from predict_page import show_predict
from explore_page import show_explore_page
def add_bg_from_url():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://www.arkanalabs.com/wp-content/uploads/2021/10/diabetes-1536x1158.png');
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
