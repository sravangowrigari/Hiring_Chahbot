from transformers import pipeline
from prompts import SYSTEM_PROMPT

llm = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-7B-Instruct",
    max_new_tokens=350,
    temperature=0.7
)

def generate_questions(tech_stack):
    prompt = f"""
{SYSTEM_PROMPT}
Tech Stack: {", ".join(tech_stack)}
"""
    return llm(prompt)[0]["generated_text"]
