def is_low_quality(text: str) -> bool:
    basic_patterns = ["what is", "define", "explain", "list"]

    questions = [q for q in text.split("\n") if q.strip()]
    if len(questions) < 3:
        return True

    for q in questions:
        if any(q.lower().startswith(p) for p in basic_patterns):
            return True

    return False
