
import streamlit as st

col1, col2, col3, col4 = st.columns((2,1,1,1))

with col1:
    st.title("This is my first app")
with col2:
    st.header("This is header")
with col3:
    st.subheader("This is subheader")
with col4:
    st.write("Now in write zone")


