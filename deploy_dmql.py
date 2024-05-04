import streamlit as st
import psycopg2
import pandas as pd

# DB conf
db_HOST = "127.0.0.1"
db_NAME = "postgres"
db_USER = "postgres"
db_PASS = "@Deep7777"

def get_conn():
    return psycopg2.connect(dbname=db_NAME, user=db_USER, password=db_PASS, host=db_HOST)

def run_query(query):
    with get_conn() as conn:
        return pd.read_sql_query(query, conn)

def main():
    st.title('E-Commerce Admin Dashboard')

    query = st.text_area("SQL query goes here:", height=200)

    if st.button("Run"):
        if query:
            try:
                result = run_query(query)
                st.write(result)
            except Exception as e:
                st.error(f"Error running query: {str(e)}")
        else:
            st.error("Enter an SQL query for execution.")

if _name_ == "_main_":
    main()
