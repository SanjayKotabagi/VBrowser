import streamlit as st


# Get the URL from the user
url = st.text_input('Enter a URL')

# Display the iFrame for the provided URL
st.markdown(f'<iframe src="{url}" width="700" height="450"></iframe>', unsafe_allow_html=True)
