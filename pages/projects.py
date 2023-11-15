import streamlit as st
import streamlit.components.v1 as components


# Set streamlit page configurations
st.set_page_config(layout="wide", 
                   initial_sidebar_state="collapsed")

# Add Custom CSS to the streamlit page
with open("assets/app.css", "r") as f:
    page_bg_img = f.read()    

st.markdown(page_bg_img, unsafe_allow_html=True)

# Contents for the Project page



st.header('My Projects', divider='rainbow')


def load_html_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

ev_wa_tableau_viz = load_html_file('./tableau_embed/ev_washington.html')
vscode_tableau_viz = load_html_file('./tableau_embed/vs_code.html')
phbanks_tableau_viz = load_html_file('./tableau_embed/ph_banks.html')


st.write('Ohhh, heart, heart, heart!!')

# Project 1: Washington Vehicle Electrification 
st.subheader('Electric Touch')
components.html(ev_wa_tableau_viz)



components.html(vscode_tableau_viz)
components.html(phbanks_tableau_viz)
