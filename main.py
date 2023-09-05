import streamlit as st


st.write("loading ...")
uploaded_file = st.file_uploader("Add text file !")
if uploaded_file:
    for line in uploaded_file:
        st.write(line)
