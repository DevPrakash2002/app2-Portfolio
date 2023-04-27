import streamlit as st
import send_email as se


st.set_page_config(layout="wide")
st.header("Contact Me")

with st.form(key= 'contact_form'):
    user_email = st.text_input('Email Id', key='mailid')
    stmessage = st.text_area('Your Message')
    message = f"""\
Subject: New Email From {user_email}

From: {user_email}
{stmessage}
    
"""
    button = st.form_submit_button()
    if button:
        se.send_email(message)
        st.info('Your Email Was Sent Successfully')