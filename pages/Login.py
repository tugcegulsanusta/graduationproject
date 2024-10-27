import streamlit as st
import sqlite3

conn = sqlite3.connect('gradPortal.sqlite3')
c= conn.cursor()
st.subheader('Welcome to Hacettepe Graduation Portal')

def login():
    with st.form("Login", clear_on_submit=True):
        email = st.text_input("Email")
        password = st.text_input("Password")
        if st.form_submit_button("Login"):
            search_user = c.execute("SELECT * FROM Users WHERE email = ? AND password = ? ", (email, password) ).fetchone()
            if search_user == None:
                st.error("Invalid Email or Password")
            else:
                pages = st.navigation([st.Page("pages/Education.py"), st.Page("pages/Job.py"), st.Page("pages/PersonalInfo.py")])
                pages.run()
login()