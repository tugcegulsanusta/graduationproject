import streamlit as st

st.header("Education")

with st.form("Add educational information", clear_on_submit=True):
    institute = st.text_input("Name of the institution: ")
    department = st.text_input("Name of the department: ")
    grade = st.number_input("GPA: ")

    submit = st.form_submit_button("Submit")
