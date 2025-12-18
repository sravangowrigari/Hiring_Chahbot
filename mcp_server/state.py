conversation_state = {}

def get_state(session_id):
    return conversation_state.setdefault(session_id, {
        "questions": [],
        "answers": [],
        "score": 0
    })
