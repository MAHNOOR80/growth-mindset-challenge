import streamlit as st

st.image("./assests/resume.png", caption="Resume Builder - Create & Download Professional Resumes", use_container_width=True)

st.title("Resume Builder Website")
st.write("The Resume Builder allows users to create personalized resumes using HTML, CSS, and JavaScript. Choose a theme, add your information, and generate your professional resume in PDF format.")

st.markdown("""
🌟 Features:
- 📝 **Customizable themes**: Choose from different professional resume templates  
- 🖋️ **Add personal information**: Input your name, experience, education, skills, and more  
- 📄 **Generate your resume** instantly  
- 💾 **Save as PDF**: Download your resume with one click  
- 🎨 **Modern UI** with easy-to-use interface
""")

if st.button("🔗 Live Demo - Resume Builder"):
    st.page_link("https://milestone5-resumebuilder-mahnoor.vercel.app/", label="🌍 Visit Resume Builder")

if st.button("🛠️ GitHub Repo - Resume Builder"):
    st.page_link("https://github.com/MAHNOOR80/milestone5-resumebuilder.git", label="📂 View GitHub Repo")
