import streamlit as st
from auth import login, check_auth
from dashboard import show_dashboard
st.set_page_config(
    page_title="AI Portfolio System",
    layout="wide"
)

# Custom CSS (simple but powerful)
st.markdown("""
    <style>
        .main {background-color: #0E1117;}
        .stMetric {background-color: #1c1f26; padding: 15px; border-radius: 10px;}
    </style>
""", unsafe_allow_html=True)

login()

if check_auth():
    st.sidebar.success(f"Welcome {st.session_state['user']}")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard"])

    if page == "Dashboard":
        show_dashboard()
else:
    st.warning("Please login to continue")