import streamlit as st
import sqlite3

conn = sqlite3.connect('gradPortal.sqlite3')
c= conn.cursor()
st.subheader('Welcome to Hacettepe Graduation Portal!')

def signup():
    with st.form("Sign Up"):
        name = st.text_input("Name")
        surname = st.text_input("Surname")
        email = st.text_input("Email")
        password = st.text_input("Password")

        if st.form_submit_button("Sign Up"):
            c.execute("INSERT INTO Users (name, surname, email, password) VALUES (?, ?, ?, ?)", (name, surname, email, password))
            conn.commit()
            st.success("You have successfully registered")
signup()