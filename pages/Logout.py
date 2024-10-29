import streamlit as st
from streamlit import button

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = True


def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.success("Logged out successfully")

st.subheader("Are you sure to be logged out?")
st.button("Yes", on_click=logout)

