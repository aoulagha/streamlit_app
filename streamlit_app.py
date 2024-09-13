import streamlit as st
import pandas as pd
import numpy as np

st.title("** Dashboard des Accidents de Voiture ** by Amine")

np.random.seed(0)
dates = pd.date_range('2015-01-01', periods=2000, freq='D')
data = {
    'Date': dates,
    'Accidents': np.random.poisson(2, size=len(dates)),
    'Weather_Condition': np.random.choice(['Clear', 'Rainy', 'Snowy', 'Foggy'], size=len(dates)),
    'Weekend': (dates.weekday >= 5).astype(int)
}
df = pd.DataFrame(data)


df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

df['Year'] = df.index.year
df['Month'] = df.index.month
df['Weekday'] = df.index.weekday

st.sidebar.title("**Formulaire**")
st.sidebar.write("Sélectionner une année :")
selected_year = st.sidebar.selectbox('Année:', df['Year'].unique())

# st.write("Liste des années disponibles :")
# result = '-'.join(map(str, df['Year'].unique()))
# st.write(result)
condition = df['Year'] == selected_year
filtre_df = df[condition]
st.write("Année sélectionnée :", selected_year)

weather_condition = st.sidebar.multiselect('Condition Météo:', df['Weather_Condition'].unique(), default=df['Weather_Condition'].unique())
filtered_df = filtre_df[filtre_df['Weather_Condition'].isin(weather_condition)]

st.write(f"Accidents avec la condition météo sélectionnée ({', '.join(weather_condition)}):")
st.write(filtered_df)

st.write(f"**Nombre total d'accidents pour l'année {selected_year}**: {filtre_df['Accidents'].sum()}")
st.write(f"**Moyenne d'accidents par jour**: {filtre_df['Accidents'].mean():.2f}")

st.sidebar.download_button(
    label="Télécharger les données",
    data=filtered_df.to_csv(),
    file_name=f"accidents_{selected_year}.csv",
    mime='text/csv',
)

footer_html = """<div style='text-align: center;'>
  <p>Developed with ❤️ by Amine</p>
</div>"""
st.markdown(footer_html, unsafe_allow_html=True)

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")



