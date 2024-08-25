import streamlit as st
import requests
import json

def process_data(data):
    # Send a POST request to the backend API
    url = "http://localhost:8000/"  # Replace with your backend API URL
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the response data
        response_data = response.json()
        return response_data
    else:
        return {"error": "Failed to process the data"}

def get_operation_code():
    # Send a GET request to the backend API
    url = "http://localhost:8000/bfhl"  # Replace with your backend API URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the response data
        response_data = response.json()
        return response_data
    else:
        return {"error": "Failed to get operation code"}

def main():
    st.title("Data Processing App")

    # Get operation code
    operation_code = get_operation_code()
    st.write("Operation Code:", operation_code)

    # Get user input
    input_data = st.text_area("Enter JSON data", placeholder='{"user_id": "123", "college_email": "example@college.edu", "college_roll_number": "2020ABC123", "numbers": [1, 2, 3], "alphabets": ["A", "B", "c"]}')

    if st.button("Process Data"):
        # Parse the input JSON
        try:
            data = json.loads(input_data)
        except json.JSONDecodeError:
            st.error("Invalid JSON format")
            return

        # Process the data
        response = process_data(data)

        # Display the response
        st.write("Response:")
        st.json(response)

if __name__ == "__main__":
    main()
