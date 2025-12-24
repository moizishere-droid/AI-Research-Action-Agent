import streamlit as st
from datetime import datetime
import os

from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import Tool
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.chat_history import InMemoryChatMessageHistory

# Notes file
NOTES_FILE = os.path.join(os.path.dirname(__file__), "agent_save.txt")

def save_note(text: str) -> str:
    """Save note with timestamp."""
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now()}] {text}\n")
    return "Note saved successfully."

def read_note(_: str = "") -> str:
    """Read all saved notes."""
    if not os.path.exists(NOTES_FILE):
        return "No notes found."
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return f.read()

# Streamlit Config
st.set_page_config(page_title="AI Agent", layout="wide")
st.title("🧠 Tool-Calling AI Agent (Modern LangChain)")

# API Key
api_key = st.sidebar.text_input(
    "Enter OpenAI API Key",
    type="password"
)

if not api_key:
    st.warning("Please enter your API key")
    st.stop()

# LLM
llm = ChatOpenAI(
    temperature=0,
    api_key=api_key
)

# Built-in Tools
search_tool = DuckDuckGoSearchRun()

def calculator(expr: str) -> str:
    try:
        return str(eval(expr))
    except Exception:
        return "Invalid expression"

calculator_tool = Tool(
    name="Calculator",
    description="Solve math expressions",
    func=calculator
)

# Custom Tools
save_note_tool = Tool(
    name="Save Note",
    description="Save important note for future reference",
    func=save_note
)

read_note_tool = Tool(
    name="Read Note",
    description="Read all saved notes",
    func=read_note
)

# Tool list
tools = [
    search_tool,
    calculator_tool,
    save_note_tool,
    read_note_tool
]

# Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = InMemoryChatMessageHistory()

def format_history(history):
    formatted = ""
    for msg in history.messages:
        if isinstance(msg, HumanMessage):
            formatted += f"Human: {msg.content}\n"
        elif isinstance(msg, AIMessage):
            formatted += f"AI: {msg.content}\n"
    return formatted

# UI
user_input = st.text_area(
    "Ask the agent:",
    placeholder=(
        "Examples:\n"
        "- Save note: Remember to check AI news daily\n"
        "- Read my saved notes\n"
        "- Calculate (45 * 12) + 7"
    )
)

if st.button("Run Agent") and user_input.strip():
    with st.spinner("Thinking..."):
        # Prepare conversation with history
        history_str = format_history(st.session_state.chat_history)
        full_input = f"{history_str}Human: {user_input}\nAI:"

        # Wrap input as HumanMessage
        human_msg = HumanMessage(content=full_input)

        # Generate response from LLM
        response = llm.generate([[human_msg]])
        ai_reply = response.generations[0][0].text

        # Check if user wants to save or read notes automatically
        if "save note" in user_input.lower():
            save_response = save_note(ai_reply)
            ai_reply += f"\n\n[Tool Action] {save_response}"

        if "read note" in user_input.lower() or "saved notes" in user_input.lower():
            notes = read_note()
            ai_reply = f"[Tool Action] Saved Notes:\n{notes}"
        else:
            # Normal LLM response
            response = llm.generate([[human_msg]])
            ai_reply = response.generations[0][0].text
            # Optionally save
            if "save" in user_input.lower():
                save_response = save_note(ai_reply)
                ai_reply += f"\n\n[Tool Action] {save_response}"


        # Save messages to memory
        st.session_state.chat_history.add_user_message(user_input)
        st.session_state.chat_history.add_ai_message(ai_reply)

    st.subheader("Final Answer")
    st.write(ai_reply)

# Memory Control
st.sidebar.divider()
if st.sidebar.button("🧹 Clear Memory"):
    st.session_state.chat_history.clear()
    st.sidebar.success("Memory cleared")

