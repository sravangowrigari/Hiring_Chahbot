import requests

MCP_SERVER_URL = "http://localhost:8000/questions"

def get_questions(session_id: str, tech_stack: list[str]):
    """
    Sends candidate tech stack to MCP server
    and retrieves technical interview questions.
    """
    payload = {
        "session_id": session_id,
        "tech_stack": tech_stack
    }

    response = requests.post(MCP_SERVER_URL, json=payload)
    response.raise_for_status()

    return response.json()
