from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
import sqlite3

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load google gemini model
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# function to retrieve query from the database

def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    for row in data:
        print(row)
    return data

# Define your prompt
prompt = [
    """
    You are an expert in converting English text/question into SQL query.
    The SQL database has the name 'users' and the following columns - id, name, age \n\n
    for example, \n Example 1: How many entries of records are present?,
    - the SQL command will be something like this SELECT COUNT(*) FROM users;
    also the sql code should not have any closing quotes eg. "" or '', in the output of end or begining.
"""
]


# sreamlit app
st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini App to retrieve SQL data")

question = st.text_input("Input: ", key='input')
submit = st.button("Ask the question")

# if submit is clicked

if submit:
    response = get_gemini_response(question, prompt)
    print('response sql query', response)
    response = read_sql_query(response, 'test.db')
    st.subheader("The Response is: ")

    for row in response:
        print(row)
        st.header(row)