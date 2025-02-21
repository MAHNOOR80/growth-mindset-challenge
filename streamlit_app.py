import streamlit as st

#page setup

about=st.Page(
    page="navigation/about.py",
    title="About Me",
    icon="👤",
    default=True,
)
project_1_page=st.Page(
    page="navigation/blogwebsite.py",
    title="Blog Website",
    icon="📝",
)
project_2_page=st.Page(
    page="navigation/chatbot.py",
    title="Chat Bot",
    icon="🤖",
)
project_3_page=st.Page(
    page="navigation/ecommerce_web.py",
    title="Ecommerce Website",
    icon="🛍️",
)
project_4_page=st.Page(
    page="navigation/resume.py",
    title="Resume Builder",
    icon="📄",
)


#shared on all pages
# st.logo("assests/logo.png",width=150)
st.sidebar.text("Made by 💌 Mahnoor Naveed")


#navigation
pg=st.navigation(
    {
        "Info":[about],
        "Projects":[project_1_page,project_2_page,project_3_page,project_4_page]
    }
)

#run navigation
pg.run()
