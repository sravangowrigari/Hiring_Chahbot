FALLBACK = {
    "python": [
        "How would you handle memory leaks in a long-running Python service?",
        "How do you design concurrency in Python APIs?"
    ],
    "django": [
        "How would you optimize ORM queries under heavy load?"
    ],
    "sql": [
        "How would you diagnose slow queries in production?"
    ]
}

def fallback_questions(stack):
    result = []
    for tech in stack:
        result.extend(FALLBACK.get(tech.lower(), []))
    return result[:5]
