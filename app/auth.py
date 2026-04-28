import streamlit as st

# Simple demo users (replace with DB later)
USERS = {
    "admin": "admin123",
    "md": "securepass"
}

def login():
    st.sidebar.title("Login")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["user"] = username
        else:
            st.sidebar.error("Invalid credentials")

def check_auth():
    return st.session_state.get("authenticated", False)