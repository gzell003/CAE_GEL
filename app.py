import streamlit as st

from config import APP_TITLE
from ui._brand import inject_branding
from ui.home import render_home

st.set_page_config(
    page_title=APP_TITLE,
    layout="wide",
)

if "saved_plans" not in st.session_state:
    st.session_state["saved_plans"] = []

inject_branding()

st.title(APP_TITLE)

st.caption(
    "Descubre planes locales antes de que el grupo pregunte qué hacer."
)

render_home()
