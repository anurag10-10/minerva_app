import streamlit as st

project_1_page = st.Page(
    "pages/streamlit_project_minerva.py",
    #title="Player Dashboard",
    icon=":material/bar_chart:",
)
about_page = st.Page(
    "pages/about_me.py",
    title="test_2",
    icon=":material/account_circle:",
    default=True,
)
project_2_page = st.Page(
    "pages/Player Dashboard.py",
    title="Player Dashboard",
    icon=":material/bar_chart:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[project_1_page, about_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [project_1_page],
        "Projects": [about_page, project_2_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/codingisfun_logo.png")
st.sidebar.markdown("@baller_metrics - Follow us on Instagram")


# --- RUN NAVIGATION ---
pg.run()
