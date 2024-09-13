import streamlit as st
import pandas as pd
import numpy as np

st.title("Formation Python")

tab1, tab2, tab3 = st.tabs(["Présentation de l'écosystème", "La SciPy Stack", "Librairies de visualisation", "Fichiers volumineux"])

with tab1:
    tab4, tab5, tab6 = st.tabs(["Guide", "Quiz sur venv", "Voir les réponses"])
    