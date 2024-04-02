import streamlit as st
import webbrowser 

url = st.text_input(label="Enter URL")
res = webbrowser.open(url)
st.write(res)
