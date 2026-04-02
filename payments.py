import streamlit as st

def payment_section():
    st.sidebar.title("💳 Upgrade")

    st.sidebar.write("Unlock Premium Features")

    st.sidebar.markdown("""
    ### 💰 Pay ₹99
    UPI: yourname@upi
    
    After payment, contact admin
    """)

    if st.sidebar.button("I have paid"):
        st.sidebar.success("Payment submitted (manual verification)")