import requests

SERVER_URL = "http://localhost:8000/questions"

def get_questions(session_id, tech_stack, experience):
    response = requests.post(
        SERVER_URL,
        json={
            "session_id": session_id,
            "tech_stack": tech_stack,
            "experience": experience
        }
    )
    response.raise_for_status()
    return response.json()
