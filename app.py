import streamlit as st


# Set streamlit page configurations
st.set_page_config(layout="wide", 
                   initial_sidebar_state="collapsed")

# Add Custom CSS to the streamlit page
with open("assets/app.css", "r") as f:
    page_bg_img = f.read()    

st.markdown(page_bg_img, unsafe_allow_html=True)

# Contents for the Home page

col1, col2 = st.columns(2)

with col1:
    with open('assets/about_me.txt', 'r', encoding='utf-8') as file:
        about_me_text = file.read()
    st.write(about_me_text)

    with open('assets/html_css.txt', 'r', encoding='utf-8') as file:
        disclaimer = file.read()
    st.markdown(disclaimer)

with col2:
    st.header('More Information:', divider='rainbow')
    st.link_button("Download My Resume", "https://drive.google.com/uc?export=download&id=15FttVlCRlPaoxG8vFBVzsp_aUStltZfY", type="primary")
    st.link_button("My Projects", "projects", type="secondary")
    st.link_button("LinkedIn", "www.linkedin.com/in/roi-jacob-olfindo-432402239", type="secondary")