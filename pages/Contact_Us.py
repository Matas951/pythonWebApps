import streamlit as st
from email_info import send_email

st.set_page_config(layout="wide", page_title="Contact Us")

st.header("Contact Us")


with st.form(key="email_form"):
    user_email = st.text_input("Your email address", key="email")
    topics = st.selectbox("With what do you need help?",
                          options=["Food", "Cars", "Pictures"])
    raw_message = st.text_area("Your message", key="message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic:{topics}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent!")

