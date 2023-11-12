import streamlit as st

# Set streamlit page configurations
st.set_page_config(layout="wide")


# Add Custom CSS to the streamlit page
with open("app.css", "r") as f:
    page_bg_img = f.read()    

st.markdown(page_bg_img, unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Contents for the Streamlit page

with col1:
    with open('about_me.txt', 'r', encoding='utf-8') as file:
        about_me_text = file.read()
    st.write(about_me_text)

    with open('html_css.txt', 'r', encoding='utf-8') as file:
        disclaimer = file.read()
    st.markdown(disclaimer)




with col2:
    st.header('More Information:')
    st.write('[Download My Resume](https://drive.google.com/uc?export=download&id=1Q-3qAiin3SeBxAJaszXkJK1e0a7qHDe5)')
    st.write('My projects')
    st.write('My contact')
