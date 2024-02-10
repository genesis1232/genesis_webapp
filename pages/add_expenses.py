import pandas as pd
import streamlit as st
import os

if not os.path.exists('data'):
    os.makedirs("data")
if not os.path.exists("data/expenses.csv"):
    expenses=pd.DataFrame(columns=["Date","categoy","Description","currency","amount"])
    expenses.to_csv("data/expenses.csv",index=False)

date=st.date_input("Date:date'📅:")
category=st.selectbox("Category"  ,("food🍅","perosnal care","travelling✈️","real estate🏠"))


desc=st.text_input("description",key="description")
curr=st.selectbox("currency",("dollars","pounds"))
amt=st.number_input("amount",max_value=99999999,step=50,key="amount")

def insert():
    insert_csv(date,category,desc,curr,amt)

def insert_csv(date,category,description,currency,amount):
    dataFrame=pd.read_csv("data/expenses.csv")
    dataFrame.loc[len(dataFrame)]=[date,category,description,currency,amount]
    dataFrame.to_csv("data/expenses.csv",index=False)
    st.balloons()






button=st.button("Add expenses💵")

if button:
    insert()

def delete():
    st.session_state.amount=0
    st.session_state.description=""

button=st.button("Clear expenses",on_click=delete)
