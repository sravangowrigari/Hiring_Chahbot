import streamlit as st
import uuid
from client.mcp_client import get_questions

st.title("🤖 TalentScout Hiring Assistant")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

st.write("Welcome! I’ll help with initial screening.")

tech = st.text_input("Enter your tech stack (comma separated)")

if st.button("Continue"):
    stack = [t.strip() for t in tech.split(",")]

    with st.spinner("Generating technical questions..."):
        result = get_questions(st.session_state.session_id, stack)

    for q in result["questions"]:
        st.chat_message("assistant").markdown(f"• {q}")
