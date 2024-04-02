import streamlit as st


url = st.text_input('Enter a URL')
if st.button('Submit'):
    st.markdown(f'<iframe src="{url}" width="1920" height="1080"></iframe>', unsafe_allow_html=True)
