import streamlit as st
import smtplib

with st.form("Send Email", clear_on_submit=True):
    email  = st.text_input("Email Address-From: ")
    reciever_email = st.text_input("Reciever Email-Address-To: ")

    subject = st.text_input("Subject: ")
    message = st.text_input("Message: ")

    text = f"Subject: {subject}\n\n{message}"
    if st.form_submit_button("Send"):

        server= smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email, "ffzromwzizljviog")

        server.sendmail(email, reciever_email, text)

        print("Email sent!")
