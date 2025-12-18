from transformers import pipeline
from .prompts import SYSTEM_PROMPT

generator = pipeline(
    "text-generation",
    model="meta-llama/Llama-3.2-1B",
    max_new_tokens=300,
    temperature=0.6,
    device_map="auto"
)

def generate_questions(tech_stack, experience):
    prompt = f"""
{SYSTEM_PROMPT}

Candidate Experience: {experience}
Tech Stack: {", ".join(tech_stack)}

Generate questions:
"""
    output = generator(prompt)[0]["generated_text"]
    return output
