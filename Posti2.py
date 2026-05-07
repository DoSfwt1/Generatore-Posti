import streamlit as st
import random
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Classroom Seat Generator", layout="wide")

# Initialize students list
studenti = [
    "Brusa", "Kalle", "Martina", "Dige", "Doyle", "Londino", "Carlo", "Arianna",
    "Sergio", "Mine", "Elena", "Veronica", "Francesca", "Cristina", "Iris",
    "Saita", "Signo", "Sammy", "Caterina", "Anna", "Peruta", "Zanoli", "Sciacca"
]

date = datetime.now()
str_date = date.strftime('%Y-%m-%d')
random.seed(str_date)

# Initialize Session State for data and shuffle
if 'data_simulata' not in st.session_state:
    st.session_state.data_simulata = date

if 'current_order' not in st.session_state:
    random.shuffle(studenti)
    st.session_state.current_order = studenti

def shuffle_seats():
    random.shuffle(studenti)
    st.session_state.current_order = studenti
    st.session_state.data_simulata += timedelta(days=1)

# Title and Date
st.title("🪑 Classroom Seating Simulator")
st.subheader(f"Disposizione del: {st.session_state.data_simulata.strftime('%d/%m/%Y')}")

# Button to generate next day
st.button("🔄 NUOVA CONFIGURAZIONE", on_click=shuffle_seats)

# Helper function to create a "Desk" look
def desk(name, color="#e1f5fe"):
    st.markdown(f"""
        <div style="
            background-color: {color};
            border: 2px solid #01579b;
            border-radius: 5px;
            padding: 10px;
            text-align: center;
            font-weight: bold;
            margin-bottom: 10px;
            color: #01579b;
            font-family: Arial;">
            {name}
        </div>
    """, unsafe_allow_html=True)

# Layout: Cattedra
st.markdown("<div style='background-color: #fb8c00; color: white; text-align: center; padding: 10px; font-weight: bold; border-radius: 5px; width: 200px; margin: 0 auto 30px auto;'>CATTEDRA</div>", unsafe_allow_html=True)

# Main Seating Layout using columns
col1, spacer1, col2, spacer2, col3 = st.columns([2, 1, 3, 1, 2])
idx = 0
current_studenti = st.session_state.current_order

# --- FILA SINISTRA (6 posti: 3 coppie) ---
with col1:
    st.write("**Fila Sinistra**")
    for r in range(3):
        c_sub1, c_sub2 = st.columns(2)
        with c_sub1: desk(current_studenti[idx])
        idx += 1
        with c_sub2: desk(current_studenti[idx])
        idx += 1

# --- FILA CENTRALE (9 posti: 3 coppie + 1 terzetto) ---
with col2:
    st.write("**Fila Centrale**")
    for r in range(3):
        c_sub1, c_sub2 = st.columns(2)
        with c_sub1: desk(current_studenti[idx])
        idx += 1
        with c_sub2: desk(current_studenti[idx])
        idx += 1
    # Terzetto finale
    c_sub1, c_sub2, c_sub3 = st.columns(3)
    for c in [c_sub1, c_sub2, c_sub3]:
        with c: desk(current_studenti[idx], color="#fff9c4")
        idx += 1

# --- FILA DESTRA (8 posti: 4 coppie) ---
with col3:
    st.write("**Fila Destra**")
    for r in range(4):
        c_sub1, c_sub2 = st.columns(2)
        if idx < len(current_studenti):
            with c_sub1: desk(current_studenti[idx])
            idx += 1
        if idx < len(current_studenti):
            with c_sub2: desk(current_studenti[idx])
            idx += 1

