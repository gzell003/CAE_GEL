import streamlit as st

from config import APP_TITLE
from ui._brand import inject_branding
from ui.home import render_home

st.set_page_config(
    page_title=APP_TITLE,
    layout="wide",
)

inject_branding()

st.title(APP_TITLE)

render_home()
