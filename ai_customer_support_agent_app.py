import streamlit as st
from agent.customer_support_engine import SupportEngine

st.title("AI Customer Support Agent")

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about returns, products, etc."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        engine = SupportEngine()
        response = engine.handle_query(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})