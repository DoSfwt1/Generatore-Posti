import streamlit as st
import random
from datetime import datetime, timedelta




st.set_page_config(page_title="Classroom Seat Generator", layout="wide")



if "admin_mode" not in st.session_state:
    st.session_state.admin_mode = False
if "show_login" not in st.session_state:
    st.session_state.show_login = False

studenti = [
    "Brusa", "Kalle", "Martina", "Dige", "Doyle", "Londino", "Carlo", "Arianna",
    "Sergio", "Mine", "Elena", "Veronica", "Francesca", "Cristina", "Iris",
    "Saita", "Signo", "Sammy", "Caterina", "Anna", "Peruta", "Zanoli", "Sciacca"
]


lenght = len(studenti)
from a import *
# 1. Calcoliamo il seed basato SOLO sulla data di oggi
# aggiungo 8 ore così che alle 16 scatti la configurazione del giorno dopo
curr_date = datetime.now() + timedelta(hours=10)

seed_date = curr_date.strftime('%d/%m/%Y')
# 2. Generiamo l'ordine fisso per oggi (senza Session State per il rimescolamento)
# In questo modo, ogni volta che la pagina carica, se la data è la stessa, l'ordine è lo stesso.
random.seed(seed_date)
random.shuffle(studenti)
lght = len(studenti)
if(lght!=lenght):
    st.error("Qualcosa è andato storto...")



col_logo, _ = st.columns([1, 4]) 
with col_logo:
    st.logo("big_brother_eye.png")

st.subheader(f"Disposizione ufficiale del: {seed_date}")

# Messaggio informativo invece del pulsante (visto che il seed rende tutto fisso)
st.info(f"La disposizione si aggiorna automaticamente ogni giorno alle 16:00.")

@st.dialog("login",dismissible=True)
def login_dialog():
        st.write("Big Brother is always watching you...")
        username = st.text_input("Username...")
        password = st.text_input("Password...",type="password")
        if st.button("login",type="primary",use_container_width=True):
            try:
                conn = st.connection("https://docs.google.com/spreadsheets/d/1_BsvQ98IHm_RDlqSiPHNBaI_WRqgHiq4IQHp80oJjh0/edit?gid=0#gid=0",
                     type="google_sheets")

                df.conn.read(ttl="1m")

                user_row = df[df["Username"]==username]

                if not user_row.empty:
                    pswd = str(user_row["Password"].values[0])
                    if(pswd==password):
                        if str(user_row["AdminStatus"].values[0])=="TRUE":
                            st.write("Login da amministratore\n avvenuto con successo")
                        else:
                            st.write("Spiacente! non sei amministratore")
                    else:
                        st.error("Password errata")
                else:
                    st.error("Username errato")

            except Exception as e:
                st.error("Errore nel caricamento dei dati. Riprova")
        



if st.session_state.show_login == True:
    if st.session_state.admin_mode == True:
        st.error("Sei già dentro come amministratore!")
    else:
        login_dialog()
        



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


with st.sidebar:
    if st.button("login",type="primary",use_container_width=True):
        st.session_state.show_login = True
        st.rerun()
    
    
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
        if idx < lenght:
            with c_sub1: desk(studenti[idx]); idx += 1
        if idx < lenght:
            with c_sub2: desk(studenti[idx]); idx += 1

