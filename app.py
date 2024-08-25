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

        # Render the response based on the logic
        if "result" in response_data:
            result = response_data["result"]
            if isinstance(result, list):
                st.write("The result is a list:")
                for item in result:
                    st.write(f"- {item}")
            elif isinstance(result, dict):
                st.write("The result is a dictionary:")
                for key, value in result.items():
                    st.write(f"{key}: {value}")
            else:
                st.write(f"The result is: {result}")
        else:
            st.write(response_data)

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
