import streamlit as st
import sqlite3
conn = sqlite3.connect('gradPortal.sqlite3')
c = conn.cursor()

st.subheader('Welcome to Hacettepe Graduation Portal!')

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    if not st.session_state.logged_in:
        with st.form("Login", clear_on_submit=True):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")

        if submitted:
            search_user = c.execute("SELECT * FROM Users WHERE email = ? AND password = ?", (email, password)).fetchone()
            if search_user is None:
                st.error("Invalid Email or Password")
            else:
                st.session_state.logged_in = True
                st.session_state.user_id = search_user[2]  # Kullanıcı ID'sini session_state'e kaydet
                st.session_state.role = search_user[6]  # Role bilgisini session_state'e kaydet
                st.success("Logged in successfully")
                st.rerun()  # Sayfayı yeniden yükleyerek oturum açılmış sayfaları göster

    else:
        if st.session_state.role == 'admin':
            pages = st.navigation([st.Page("pages/Admin.py"), st.Page("pages/Mail.py"), st.Page("pages/Logout.py")])
            pages.run()
        else:
            pages = st.navigation([st.Page("pages/Education.py"), st.Page("pages/Job.py"), st.Page("pages/PersonalInfo.py"), st.Page("pages/Logout.py")])
            pages.run()

login()