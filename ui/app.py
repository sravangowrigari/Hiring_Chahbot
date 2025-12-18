import streamlit as st
from mcp_client.client import fetch_questions

st.title("🤖 Hiring Assistant Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

tech = st.text_input("Enter Tech Stack (comma separated)")
exp = st.selectbox("Experience", ["1-3 years", "3-5 years", "5+ years"])

if st.button("Generate Questions"):
    tech_stack = [t.strip() for t in tech.split(",")]

    with st.chat_message("assistant"):
        with st.spinner("Generating advanced interview questions..."):
            result = fetch_questions(tech_stack, exp)

    for q in result["questions"]:
        st.chat_message("assistant").markdown(f"• {q}")
