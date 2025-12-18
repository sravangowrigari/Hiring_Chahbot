FALLBACK_QUESTIONS = {
    "python": [
        "How would you debug memory leaks in a long-running Python service?",
        "How do you handle concurrency in Python APIs?"
    ],
    "django": [
        "How would you manage database migrations with zero downtime?"
    ],
    "sql": [
        "How would you identify and optimize slow queries in production?"
    ],
    "docker": [
        "How do you reduce Docker image size without impacting performance?"
    ]
}

def get_fallback(tech_stack):
    result = []
    for tech in tech_stack:
        result.extend(FALLBACK_QUESTIONS.get(tech.lower(), []))
    return result[:5]
