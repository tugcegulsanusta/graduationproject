import streamlit as st

st.set_page_config(page_title="Grad Portal", page_icon=":graduation_cap:", layout="wide")

st.header('Grad Portal')
    # Create login form

def defaultPage():
    pages = st.navigation([st.Page("pages/Login.py"), st.Page("pages/Signup.py")])
    pages.run()

if __name__ == '__main__':
    defaultPage()
#pg = st.navigation([st.Page("pages/Education.py"), st.Page("pages/Job.py"), st.Page("pages/PersonalInfo.py")])
#pg.run()