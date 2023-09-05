import streamlit as st
import request

st.write("loading ...")
file = request.get("https://github.com/r2010shadow/appless/blob/main/upload-case.py")
st.write(file)
