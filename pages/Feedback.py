import streamlit as st
name=st.text_input("Name")
feedabck=st.text_input("feeback")
rating=st.slider("Rating",min_value=1,max_value=5)
if rating==1:
    st.subheader("please rate more higher")
if rating==2:
    st.subheader("Not the greates rating")
if rating==3:
    st.subheader("average")
if rating==4:
    st.subheader("good score")
if rating==5:
    st.subheader("Thank you fo your services")
button=st.button("submit")

st.ballons()





