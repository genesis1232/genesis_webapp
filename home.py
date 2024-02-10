import streamlit as st
tab1,tab2,tab3=st.tabs(["About","Hobbies","Contact"])
tab2.write("Cricket,Football,")
tab3.write("email: genesis@gmail.com")
tab3.write("phone number: 77037932")
with tab1:
    col1,col2=st.columns([0.3,0.7])
    with col1:
        st.image("images/geneis 12th.jpg",width=200)
        st.subheader("Genesis")