from transformers import pipeline
from .prompts import SYSTEM_PROMPT

generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-7B-Instruct",
    max_new_tokens=400,
    temperature=0.7
)

def generate_questions(tech_stack, experience):
    prompt = f"""
{SYSTEM_PROMPT}

Candidate Experience: {experience}
Tech Stack: {", ".join(tech_stack)}

Generate questions:
"""

    response = generator(prompt)[0]["generated_text"]
    return response
