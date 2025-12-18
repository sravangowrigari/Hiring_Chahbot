def is_low_quality(text: str) -> bool:
    bad_starts = ("what is", "define", "explain", "list")
    questions = [q.strip() for q in text.split("\n") if q.strip()]

    if len(questions) < 3:
        return True

    for q in questions:
        if q.lower().startswith(bad_starts):
            return True

    return False
