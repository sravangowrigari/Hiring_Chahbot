from fastapi import FastAPI
from pydantic import BaseModel

from llm import generate_questions
from validator import is_low_quality
from fallback import get_fallback

app = FastAPI()

class Request(BaseModel):
    session_id: str
    tech_stack: list[str]
    experience: str
    answer: str | None = None

@app.post("/generate")
def generate(req: Request):
    text = generate_questions(req.tech_stack, req.experience)

    if text.strip() == "LOW_CONFIDENCE" or is_low_quality(text):
        return {
            "source": "fallback",
            "questions": get_fallback(req.tech_stack)
        }

    return {
        "source": "ai",
        "questions": text.split("\n")
    }
from state import get_state

@app.post("/chat")
def chat(req: Request):
    state = get_state(req.session_id)

    if req.answer:
        state["answers"].append(req.answer)

    # generate next question
