import sqlite3

import streamlit as st

conn = sqlite3.connect("gradPortal.sqlite3")
c = conn.cursor()

st.header("Users")

option = st.selectbox("Filter Users By", ["Graduation Year", "Job Type"])
if option == "Graduation Year":
    filter = st.text_input("Graduation Year")
    result = c.execute("""
        SELECT Users.email
        FROM JobInfo
        JOIN Users ON JobInfo.user_id = Users.user_id
        WHERE JobInfo.Graduation_Year = ?
    """, (filter,))
    emails = result.fetchall()
    for email in emails:
        st.write(email)