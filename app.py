import streamlit as st

# Set streamlit page configurations
st.set_page_config(layout="wide",
                   page_icon="app_icon.png",
                   page_title='Internship Proposal',
                   initial_sidebar_state="collapsed")

# Add Custom CSS to the streamlit page
try:
    with open("css/app.css", "r") as f:
        page_bg_img = f.read()    
    st.markdown(page_bg_img, unsafe_allow_html=True)
except FileNotFoundError:
    st.error("File 'app.css' not found. Ensure it's in the correct directory.")

# Function to read file content
def read_file(file_path):
    """Reads text from a file and returns it."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file at '{file_path}' was not found."

# Contents for the Home page
col1, col2 = st.columns(2)

# Column 1: About Me and Site Disclaimer
with col1:
    about_me = read_file('text_files/about_me.txt')
    st.write(about_me)
    site_disclaimer = read_file('text_files/html_css.txt')
    st.markdown(site_disclaimer)

# Column 2: Additional Information and Links
with col2:
    st.header('More Information:', divider='rainbow')
    st.link_button("Download My Resume", "https://drive.google.com/file/d/1Z5lurx9Xc4oKEIR7R5SZytXE4_hnbpoW/view?usp=sharing", type="primary")
    # st.link_button("Download My CV", "https://drive.google.com/uc?export=download&id=1u8CF3Y--JlP7OpXQv7g92CS5VdhsAtSQ", type="secondary")
    st.link_button("Personal/Professional Blogs (Coming Soon)", "none", type="secondary")
    st.link_button("My Projects", "projects", type="secondary")
    st.link_button("LinkedIn", "https://www.linkedin.com/in/roi-jacob-olfindo-432402239", type="secondary")
    st.link_button("GitHub", "https://github.com/roijacob", type="secondary")