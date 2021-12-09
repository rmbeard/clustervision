# Adapted by Rachel Beard, last updated 12/9/21
import streamlit as st
from multiapp import MultiApp
from apps import (
    home,
    cluster2,
    forecast,
    survey
)

st.set_page_config(page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
apps = MultiApp()

# Add applications here

apps.add_app("Home", home.app)
##apps.add_app("Cluster", cluster.app)
apps.add_app("Cluster", cluster2.app)
apps.add_app("Forecast", forecast.app)
apps.add_app("Survey", survey.app)

# The main app
apps.run()
