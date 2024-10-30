import streamlit as st
import sqlite3
from pages.Education import submit

conn = sqlite3.connect('gradPortal.sqlite3')
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS JobInfo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        job_title TEXT,
        job_type TEXT,
        job_start_date DATE,
        job_end_date DATE,
        user_id INTEGER
    )
""")
conn.commit()

st.header("Job History")
option = st.selectbox("Choose: ", ["Add Job", "Show Job History"])

if option == "Add Job":
    if 'user_id' in st.session_state:
        with st.form("Add Job History", clear_on_submit=True):
            company_name = st.text_input("Company Name: ")
            job_title = st.text_input("Job Title: ")
            job_type = st.selectbox("Job Type: ", ["Private Sector", "Public Sector"])
            job_start_date = st.date_input("Job Start Date: ")
            job_end_date = st.date_input("Job End Date: ")

            if st.form_submit_button("Submit"):
                user_id = st.session_state["user_id"]
                c.execute("INSERT INTO JobInfo (company_name, job_title, job_type, job_start_date, job_end_date, user_id) VALUES (?,?,?,?,?,?)",
                          (company_name, job_title, job_type, job_start_date, job_end_date, user_id))
                conn.commit()
                st.success("Job history submitted successfully!")
    else:
        st.warning("Please log in to add job history.")

elif option == "Show Job History":
    if 'user_id' in st.session_state:
        user_id = st.session_state["user_id"]
        result = c.execute("SELECT company_name, job_title, job_type, job_start_date, job_end_date FROM JobInfo WHERE user_id=?", (user_id,))
        job_history = result.fetchall()
        if job_history:
            st.write(job_history)
        else:
            st.info("No job history found.")
    else:
        st.warning("Please log in to view job history.")