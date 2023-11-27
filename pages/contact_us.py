import streamlit as st


st.header("Contact Me")

with st.form():
    user_email = st.text_input("Your Email Address")
    message = st.text_area("your message")
    button = st.form_submit_button("Submit")
    
