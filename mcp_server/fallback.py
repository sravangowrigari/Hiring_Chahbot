FALLBACK_QUESTIONS = {
    "python": [
        "How would you debug a memory leak in a long-running Python service?",
        "How do you design concurrency handling in a Python API under heavy load?"
    ],
    "fastapi": [
        "How would you manage dependency injection and lifecycle events in FastAPI?",
    ],
    "sql": [
        "How would you optimize a query that performs well in dev but fails in prod?"
    ],
    "docker": [
        "How do you reduce Docker image size without impacting runtime performance?"
    ]
}

def get_fallback(tech_stack):
    result = []
    for tech in tech_stack:
        key = tech.lower()
        if key in FALLBACK_QUESTIONS:
            result.extend(FALLBACK_QUESTIONS[key])
    return result[:5]
