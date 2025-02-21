import streamlit as st
import re

# Email validation function
def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None

# Contact form function
def contact_form():
    st.title("📩 Contact Us")

    with st.form("contact_form"):
        # Form fields with emojis
        name = st.text_input("👤 First Name")
        email = st.text_input("📧 Email Address")
        message = st.text_area("💬 Your Message")
        
        submit_button = st.form_submit_button("📩 Submit")

        if submit_button:
            # Validate user input
            if not name:
                st.error("❌ Please provide your name.")
                st.stop()

            if not email:
                st.error("❌ Please provide your email address.")
                st.stop()

            if not is_valid_email(email):
                st.error("❌ Please provide a valid email address.")
                st.stop()

            if not message:
                st.error("❌ Please provide a message.")
                st.stop()

            # Show success message
            st.success("✅ Your message has been sent successfully!")

