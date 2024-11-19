import streamlit as st
import pandas as pd

# Start med å lage en tom DataFrame for treningsloggen
if "logg" not in st.session_state:
    st.session_state["logg"] = pd.DataFrame(columns=["Dag", "Øvelse", "Sett", "Reps", "Vekt", "Notater"])

st.title("Treningslogg")

# Velg dag
dag = st.selectbox("Velg treningsdag", ["Bryst, skuldre og triceps", "Rygg og biceps", "Bein og kjerne"])

# Velg øvelse basert på dagen
øvelser = {
    "Bryst, skuldre og triceps": ["Benkpress", "Skrå hantelpress", "Sidehev", "Skulderpress", "Franskpress", "Dips"],
    "Rygg og biceps": ["Markløft", "Pull-ups", "Stående roing", "Face pulls", "Bicepscurl", "Hammercurls"],
    "Bein og kjerne": ["Knebøy", "Utfall", "Rumensk markløft", "Leg curl", "Stående legghev", "Hanging leg raises"]
}
øvelse = st.selectbox("Velg øvelse", øvelser[dag])

# Input for loggføring
sett = st.number_input("Antall sett", min_value=1, max_value=10, value=3)
reps = st.number_input("Antall reps per sett", min_value=1, max_value=50, value=10)
vekt = st.text_input("Vekt (kg)", placeholder="F.eks. 20kg eller kroppsvekt")
notater = st.text_area("Notater", placeholder="Skriv eventuelle notater her...")

# Legg til knapp for å lagre logg
if st.button("Legg til i loggen"):
    ny_rad = {"Dag": dag, "Øvelse": øvelse, "Sett": sett, "Reps": reps, "Vekt": vekt, "Notater": notater}
    st.session_state["logg"] = pd.concat([st.session_state["logg"], pd.DataFrame([ny_rad])], ignore_index=True)
    st.success("Øvelse lagt til!")

# Vis treningsloggen
st.subheader("Din treningslogg")
st.dataframe(st.session_state["logg"])

# Last ned loggen som CSV
st.download_button(
    label="Last ned treningslogg",
    data=st.session_state["logg"].to_csv(index=False),
    file_name="treningslogg.csv",
    mime="text/csv",
)
