import streamlit as st
import sqlite3
from pages.Education import submit


conn = sqlite3.connect('gradPortal.sqlite3')
c= conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS JobInfo (
        company_name TEXT,
        job_title TEXT,
        job_type TEXT,
        job_start_date DATE,
        job_end_date DATE
    )
""")
conn.commit()


st.header("Job History")
option = st.selectbox("Choose: ", ["Add Job", "Show Job History"])

if option == "Add Job":
    with st.form("Add Job History", clear_on_submit=True):
        company_name = st.text_input("Company Name: ")
        job_title = st.text_input("Job Title: ")
        job_type = st.selectbox("Job Type: ", ["Private Sector", "Public Sector"])
        job_start_date = st.date_input("Job Start Date: ")
        job_end_date = st.date_input("Job End Date: ")

        # Submit butonu ile formu gönderme işlemi
        if st.form_submit_button("Submit"):
            st.success("Job history submitted successfully!")
