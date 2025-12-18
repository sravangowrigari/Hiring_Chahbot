sessions = {}

def get_session(session_id):
    return sessions.setdefault(session_id, {
        "step": 0,
        "data": {}
    })
