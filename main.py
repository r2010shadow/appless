import streamlit as st
import pandas as pd

#col1, col2, col3, col4 = st.columns((2,1,1,1))


st.title("This is my first app")

st.header("This is header")

st.subheader("This is subheader")

st.write("Now in write zone")


df = load_data("https://github.com/r2010shadow/appless/blob/main/main.py")
st.write(df)

