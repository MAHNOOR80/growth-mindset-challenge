import streamlit as st

st.image("./assests/blog ss.png", caption="Home & Dining Decor Blog", use_container_width=True)


st.title("Blog Website")
st.write("A modern and user-friendly blog website for sharing articles and insights on home and dining decor. Built with Next.js and Tailwind CSS.")
st.markdown("""
🌟 Features:
- 📝 **Users can comment** on blog posts  
- 🔍 **SEO-optimized** for better search ranking  
- 📱 **Fully responsive** (works on mobile & desktop)  
- 🎨 **Modern UI** with clean design 
             """)


if st.button("🔗 Live Demo - Blog Website"):
    st.page_link("https://nextjs-blog-website-119n.vercel.app/",label="🌍 Visit Blog Website")

if st.button("🛠️ GitHub Repo - Blog Website"):
    st.page_link("https://github.com/MAHNOOR80/Nextjs-blog-website.git",label="📂 View GitHub Repo")


