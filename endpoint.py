from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/bfhl")
async def get_operation_code():
    response = {
        "operation_code": 1
    }
    return response

@app.post("/")
async def process_request(request: Request):
    # Get the request body
    body = await request.json()

    # Extract the required data from the request body
    user_id = body.get("user_id", "")
    college_email = body.get("college_email", "")
    college_roll_number = body.get("college_roll_number", "")
    numbers = body.get("numbers", [])
    alphabets = body.get("alphabets", [])

    # Find the highest lowercase alphabet
    lowercase_alphabets = [char for char in alphabets if char.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else ""

    # Prepare the response
    response = {
        "status": "success",
        "user_id": user_id,
        "college_email": college_email,
        "college_roll_number": college_roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

    return response
