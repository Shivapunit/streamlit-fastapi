import streamlit as st
import requests
import json

def process_data(data):
    # Send a POST request to the backend API
    url = "http://your-api-url.com/endpoint"  # Replace with your backend API URL
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the response data
        response_data = response.json()
        return response_data
    else:
        return {"error": "Failed to process the data"}

def render_response(response_data):
    if "error" in response_data:
        st.error(response_data["error"])
    else:
        st.success("Data processed successfully!")
        st.json(response_data)

def main():
    st.title("Data Processing App")

    # Get user input
    input_data = st.text_area("Enter JSON data", placeholder='{"data": ["A", "C", "z"]}')

    if st.button("Process Data"):
        # Parse the input JSON
        try:
            data = json.loads(input_data)
        except json.JSONDecodeError:
            st.error("Invalid JSON format")
            return

        # Process the data
        response = process_data(data)

        # Render the response
        render_response(response)

if __name__ == "__main__":
    main()
