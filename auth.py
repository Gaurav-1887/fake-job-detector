import streamlit as st
from db import add_user, login_user

def auth():
    st.sidebar.title("🔐 Login / Signup")

    menu = st.sidebar.selectbox("Select", ["Login", "Signup"])

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if menu == "Signup":
        if st.sidebar.button("Create Account"):
            add_user(username, password)
            st.sidebar.success("Account Created ✅")

    if menu == "Login":
        if st.sidebar.button("Login"):
            user = login_user(username, password)
            if user:
                st.session_state["user"] = username
                st.sidebar.success("Logged in ✅")
            else:
                st.sidebar.error("Invalid credentials ❌")

    return st.session_state.get("user", None)