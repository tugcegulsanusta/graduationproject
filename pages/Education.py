import streamlit as st
import sqlite3

conn = sqlite3.connect('gradPortal.sqlite3')
c= conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS Education (
        institute TEXT,
        department TEXT,
        grade REAL,
        graduation_date DATE
            )
""")
conn.commit()

st.header("Education")

with st.form("Add educational information", clear_on_submit=True):
    institute = st.text_input("Name of the institution: ")
    department = st.text_input("Name of the department: ")
    graduation_date = st.date_input("Graduation Date: ")
    grade = st.number_input("GPA: ")

    submit = st.form_submit_button("Submit")
