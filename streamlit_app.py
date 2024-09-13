import streamlit as st
import pandas as pd
import numpy as np

st.title("Formation Python")

tab1, tab2, tab3, tab4 = st.tabs(["Présentation de l'écosystème", "La SciPy Stack", "Librairies de visualisation", "Fichiers volumineux"])

with tab1:
    tab11, = st.tabs(["Guide"])

    with tab11:
        st.title("Guide de Gestion des Environnements Python avec venv")
