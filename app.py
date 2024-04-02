import streamlit as st
import webbrowser 

url = st.text_input(label="Enter URL")
st.write("Results for : ",url)
st.write(webbrowser.open(url))
