import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/api/openapiRequest"


def get_response_from_api(prompt):
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"


st.title("API Request with Streamlit")

st.write("Enter a prompt and click the button to get a response.")

user_prompt = st.text_area("Your Prompt", "")

if st.button("Send Prompt to API"):
    if user_prompt:
        with st.spinner("Sending request..."):
            response = get_response_from_api(user_prompt)

        st.write("**Response**")
        st.write(response['response'])
    else:
        st.warning("Please enter a prompt.")
