def is_low_quality(text):
    bad_starts = ["what is", "define", "explain", "list"]
    questions = text.split("\n")

    if len(questions) < 3:
        return True

    for q in questions:
        if q.lower().startswith(tuple(bad_starts)):
            return True

    return False
