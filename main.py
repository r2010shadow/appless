import streamlit as st

# Add title and Write in

st.title('That is my app.')
st.write("Streamlit is an awesome tools.")

import streamlit as st
number = st.slider("Pick a number: ", min_value=1, max_value=10)
st.text("Your number is " + str(number))
