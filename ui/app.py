import streamlit as st
import uuid
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from client.mcp_client import get_questions

st.title("🤖 TalentScout Hiring Assistant")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

st.write("Welcome! I’ll guide you through an initial screening.")

tech = st.text_input("Enter your tech stack (comma separated)")
experience = st.selectbox("Years of experience", ["1-3", "3-5", "5+"])

if st.button("Generate Questions"):
    stack = [t.strip() for t in tech.split(",") if t.strip()]

    with st.spinner("Generating technical questions..."):
        result = get_questions(
            st.session_state.session_id,
            stack,
            experience
        )

    for q in result["questions"]:
        st.chat_message("assistant").markdown(f"• {q}")
