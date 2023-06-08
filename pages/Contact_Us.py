import streamlit as st
from email_info import send_email

st.set_page_config(layout="wide", page_title="Contact Us")

st.header("Contact Us")


with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent!")
