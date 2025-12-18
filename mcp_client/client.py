import requests

def fetch_questions(tech_stack, experience):
    response = requests.post(
        "http://localhost:8000/generate",
        json={
            "tech_stack": tech_stack,
            "experience": experience
        }
    )
    return response.json()
