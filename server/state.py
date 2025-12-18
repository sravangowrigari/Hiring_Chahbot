sessions = {}

def get_session(session_id):
    return sessions.setdefault(session_id, {
        "info": {},
        "questions": []
    })
