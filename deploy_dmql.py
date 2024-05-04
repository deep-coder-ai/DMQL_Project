import streamlit as st
import psycopg2
import pandas as pd

DB_HOST = "127.0.0.1"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "@Deep7777"

def connect_to_database():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

def execute_sql_query(sql):
    with connect_to_database() as connection:
        return pd.read_sql_query(sql, connection)

def run_query_interface():
    purple_theme = {
        'base': 'light',
        'primaryColor': '#9467bd',
        'backgroundColor': '#f7f4f9',
        'secondaryBackgroundColor': '#d4b9da',
        'textColor': '#3f007d',
        'font': 'sans serif'
    }
    st.set_page_config(page_title='Database Query Tool', layout='wide')
    st.experimental_set_theme(purple_theme)

    st.header('Database Query Tool')

    user_query_text = st.text_area("SQL Query", height=150, placeholder="Write your SQL query here...")

    if st.button("Run Query"):
        if user_query_text:
            try:
                query_output = execute_sql_query(user_query_text)
                st.dataframe(query_output)
            except Exception as error:
                st.error(f"Failed to execute query: {error}")
        else:
            st.error("Enter an SQL query to run.")

if _name_ == "_main_":
    run_query_interface()
