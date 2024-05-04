import streamlit as st
import psycopg2
import pandas as pd

def establish_connection():
    # Database configuration
    HOST = "127.0.0.1"
    NAME = "postgres"
    USER = "postgres"
    PASS = "@Deep7777"
    # Establishing connection
    return psycopg2.connect(dbname=NAME, user=USER, password=PASS, host=HOST)

def execute_query(query, connection):
    return pd.read_sql_query(query, connection)

def get_user_input():
    st.title('E-Commerce Admin Dashboard')
    user_query = st.text_area("Enter SQL query here:", height=200)
    return user_query

def display_results(result):
    st.write(result)

def main():
    user_query = get_user_input()

    if st.button("Run Query"):
        if user_query:
            try:
                with establish_connection() as conn:
                    query_result = execute_query(user_query, conn)
                    display_results(query_result)
            except Exception as e:
                st.error(f"Error executing query: {str(e)}")
        else:
            st.error("Please enter an SQL query.")

if __name__ == "__main__":
    main()
