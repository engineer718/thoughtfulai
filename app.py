import streamlit as st
from utils import get_hardcoded_answer, get_fallback_answer

st.set_page_config(page_title="Thoughtful AI Support", layout="centered")
st.title("💬 Thoughtful AI Support Agent")

user_input = st.text_input("Ask me anything about Thoughtful AI:", key="input")

if user_input:
    with st.spinner("Thinking..."):
        answer = get_hardcoded_answer(user_input)
        if not answer:
            answer = get_fallback_answer(user_input)
    st.markdown("#### 🤖 Answer")
    st.write(answer)
