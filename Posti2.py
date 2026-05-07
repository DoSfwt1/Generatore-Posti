import streamlit as st
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Classroom Seat Generator", layout="wide")

studenti = [
    "Brusa", "Kalle", "Martina", "Dige", "Doyle", "Londino", "Carlo", "Arianna",
    "Sergio", "Mine", "Elena", "Veronica", "Francesca", "Cristina", "Iris",
    "Saita", "Signo", "Sammy", "Caterina", "Anna", "Peruta", "Zanoli", "Sciacca"
]

# 1. Calcoliamo il seed basato SOLO sulla data di oggi
# aggiungo 8 ore così che alle 16 scatti la configurazione del giorno dopo
curr_date = datetime.now() + timedelta(hours=8)

seed_date = curr_date.strftime('%d/%m/%Y')
# 2. Generiamo l'ordine fisso per oggi (senza Session State per il rimescolamento)
# In questo modo, ogni volta che la pagina carica, se la data è la stessa, l'ordine è lo stesso.
random.seed(seed_date)
random.shuffle(studenti)

# Titolo e Data
st.title("🪑 Classroom Seating Simulator")
st.subheader(f"Disposizione ufficiale del: {seed_date}")

# Messaggio informativo invece del pulsante (visto che il seed rende tutto fisso)
st.info(f"La disposizione si aggiorna automaticamente ogni giorno a mezzanotte.")

def desk(name, color="#e1f5fe"):
    st.markdown(f"""
        <div style="background-color: {color}; border: 2px solid #01579b; border-radius: 5px;
            padding: 10px; text-align: center; font-weight: bold; margin-bottom: 10px;
            color: #01579b; font-family: Arial;">
            {name}
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='background-color: #fb8c00; color: white; text-align: center; padding: 10px; font-weight: bold; border-radius: 5px; width: 200px; margin: 0 auto 30px auto;'>CATTEDRA</div>", unsafe_allow_html=True)

col1, spacer1, col2, spacer2, col3 = st.columns([2, 1, 3, 1, 2])
idx = 0

with col1:
    st.write("**Fila Sinistra**")
    for r in range(3):
        c_sub1, c_sub2 = st.columns(2)
        with c_sub1: desk(studenti[idx]); idx += 1
        with c_sub2: desk(studenti[idx]); idx += 1

with col2:
    st.write("**Fila Centrale**")
    for r in range(3):
        c_sub1, c_sub2 = st.columns(2)
        with c_sub1: desk(studenti[idx]); idx += 1
        with c_sub2: desk(studenti[idx]); idx += 1
    c_sub1, c_sub2, c_sub3 = st.columns(3)
    for c in [c_sub1, c_sub2, c_sub3]:
        with c: desk(studenti[idx], color="#fff9c4"); idx += 1

with col3:
    st.write("**Fila Destra**")
    for r in range(4):
        c_sub1, c_sub2 = st.columns(2)
        if idx < len(studenti):
            with c_sub1: desk(studenti[idx]); idx += 1
        if idx < len(studenti):
            with c_sub2: desk(studenti[idx]); idx += 1

