import streamlit as st

st.image("./assests/avion.png", caption="Avion - Furniture & Home Decor", use_container_width=True)

st.title("Avion eCommerce Website")
st.write("Avion is an online marketplace for high-quality furniture and home decor. Built with Next.js, Tailwind CSS, Stripe for payments, and authentication.")

st.markdown("""
🌟 Features:
- 🛒 **Shop premium furniture**: Chairs, Tables, and other home decor items  
- 💳 **Secure payments** with Stripe  
- 🔒 **User authentication**: Sign up and log in for a personalized shopping experience  
- 📱 **Fully responsive** (works on mobile & desktop)  
- 🎨 **Modern UI** with a clean design and easy navigation
""")

if st.button("🔗 Live Demo - Avion Marketplace"):
    st.page_link("https://giaic-hackathon-project-j4ln.vercel.app/", label="🌍 Visit Avion Marketplace")

if st.button("🛠️ GitHub Repo - Avion Marketplace"):
    st.page_link("https://github.com/MAHNOOR80/Giaic_Hackathon_project.git", label="📂 View GitHub Repo")
