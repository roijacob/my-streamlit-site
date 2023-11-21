import streamlit as st
import streamlit.components.v1 as components

def set_streamlit_config():
    """Set Streamlit page configuration."""
    st.set_page_config(layout="wide",
                    page_icon="app_icon.png",
                    page_title='Projects',
                    initial_sidebar_state="collapsed")

def read_file(file_path):
    """Read content from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_projects(file_names):
    """Load project descriptions from files."""
    projects = {}
    for file_name in file_names:
        project_key = file_name.split('_')[0]
        projects[project_key] = read_file(f'text_files/{file_name}')
    return projects

def display_project(header, project_desc, tableau_viz):
    """Display a project section."""
    st.subheader(header, divider='rainbow')
    st.write(project_desc)
    components.html(tableau_viz)
    st.markdown("")

# Set up the Streamlit page
set_streamlit_config()

# Add custom CSS
custom_css = read_file("app.css")
st.markdown(custom_css, unsafe_allow_html=True)

# Load project descriptions
project_intro = read_file('text_files/project_description.txt')
project_files = ['proj1_desc.txt', 'proj2_desc.txt', 'proj3_desc.txt']
projects = load_projects(project_files)

# Load Tableau visualizations
ev_wa_tableau_viz = read_file('./tableau_embed/ev_washington.html')
vscode_tableau_viz = read_file('./tableau_embed/vs_code.html')
phbanks_tableau_viz = read_file('./tableau_embed/ph_banks.html')

# Display the Project page header
st.header('My Projects', divider='rainbow')
st.write(project_intro)

# Display each project
display_project('[Vehicle Electrification of Washington :flag-us:](https://public.tableau.com/views/WashingtonGoingElectric/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link)', 
                projects['proj1'], ev_wa_tableau_viz)

display_project('[Demographics of Visual Studio Code Users :computer:](https://public.tableau.com/views/TheCultofVisualStudioCode-2/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link)', 
                projects['proj2'], vscode_tableau_viz)

display_project('[How :flag-ph: :bank: Could Improve their :apple: Application](https://public.tableau.com/views/HowPHBanksCouldImprove/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link)', 
                projects['proj3'], phbanks_tableau_viz)

st.link_button("Home", "https://streamlit-powered-apps-49142faef422.herokuapp.com/", type="primary")