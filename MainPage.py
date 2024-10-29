import streamlit as st

st.set_page_config(page_title="Grad Portal", page_icon=":graduation_cap:", layout="wide")


def main():
    pages = st.navigation([st.Page("pages/Login.py"), st.Page("pages/Signup.py")])
    pages.run()

main()