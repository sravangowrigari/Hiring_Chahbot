from fastapi import FastAPI
from pydantic import BaseModel
from llm import generate_questions
from validator import is_low_quality
from fallback import fallback_questions
from state import get_session

app = FastAPI()

class ChatRequest(BaseModel):
    session_id: str
    tech_stack: list[str]

@app.post("/questions")
def questions(req: ChatRequest):
    text = generate_questions(req.tech_stack)

    if text.strip() == "LOW_CONFIDENCE" or is_low_quality(text):
        return {
            "source": "fallback",
            "questions": fallback_questions(req.tech_stack)
        }

    return {
        "source": "ai",
        "questions": text.split("\n")
    }
