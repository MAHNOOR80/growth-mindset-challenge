import streamlit as st
from forms.contact import contact_form

def show_contact_form():
    with st.expander("📧 Contact Me", expanded=True):
        contact_form() # Assuming this renders the contact form

# Function to encode the image to Base64
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded_string}"

# Get Base64 image data
image_base64 = get_base64_image("./assests/myimage.jpg")

# Apply CSS for round image
st.markdown(
    f"""
    <style>
        .profile-pic {{
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Hero section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.markdown(f'<img src="{image_base64}" class="profile-pic">', unsafe_allow_html=True)
with col2:
    st.title("Mahnoor Naveed", anchor=False)
    st.write("Frontend Developer | Creating sleek and responsive web experiences")
    if st.button("📧 Contact Me"):
        show_contact_form()  # This will open the expander with the form

# Experience and Qualification 
st.write("\n")
st.subheader("Experience and Qualification", anchor=False)
st.markdown(
    """
    - **Frontend Developer**: Proficient in HTML, CSS, JavaScript, TypeScript, and Tailwind CSS.  
    - **UI Developer**: Experience in building pixel-perfect, responsive web apps with Next.js.  
    - **Medical Student**: Strong analytical and problem-solving skills.  
    - **Certified Web Developer**: Completed multiple web development projects and certifications.  
    """
)

# Skills
st.write("\n")
st.subheader("Skills", anchor=False)
st.markdown(
    """
    - **Programming Languages**: HTML, CSS, JavaScript, TypeScript.  
    - **Frameworks & Libraries**: Next.js, Tailwind CSS.  
    - **Design & Tools**: Figma, Canva, MS Office.  
    - **Other Skills**: Data Entry, UI/UX Design, Web Development.  
    """
)

# Projects
st.write("\n")
st.subheader("Projects", anchor=False)
st.markdown(
    """
    - **Countdown Timer App**: Built using Next.js and Tailwind CSS.  
    - **Blog Website**: Developed a fully responsive blog website.  
    - **E-commerce Store**: Created with Next.js and Tailwind CSS, featuring payment integration and authentication.  
    - **Portfolio Website**: Showcasing my skills and projects in a sleek design.  
    """
)

# Download Resume Button
resume_path = "./assests/resume.pdf"  # Assuming your resume is saved locally
st.write("\n")
st.subheader("Download My Resume", anchor=False)

with open(resume_path, "rb") as resume_file:
    st.download_button(
        label="Download Resume",
        data=resume_file,
        file_name="Mahnoor_Naveed_Resume.pdf",  # Specify file name for download
        mime="application/pdf",  # MIME type for PDF
        use_container_width=True
    )
