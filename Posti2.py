import streamlit as st
import random
from datetime import datetime, timedelta
from streamlit_gsheets import GSheetsConnection



st.set_page_config(page_title="Classroom Seat Generator", layout="wide")


if "logged" not in st.session_state:
    st.session_state.logged=False
if "admin" not in st.session_state:
    st.session_state.admin=False
if "seat" not in st.session_state:
    st.session_state.seat = " "


def signo(list):
    signo_idx=list.index("Signo")
    list[6],list[signo_idx]=list[signo_idx],list[6]

@st.dialog("LOGIN",dismissible=False)
def login_dialog():
        st.write("ACCEDI")
        username = st.text_input("USERNAME...")
        password = st.text_input("PASSWORD...",type="password")
        if st.button("login",type="primary",use_container_width=True):
            try:
                conn = st.connection("gsheets", type=GSheetsConnection)   
                table = conn.read(ttl="1m")
                table.dropna()
                
                user_row = table[table["Username"]==username]
                st.write(user_row)
                if user_row.empty == False:
                    if user_row["Password"].values[0]==password:
                        st.session_state.logged = True
                        if user_row["AdminStatus"].values[0] == True:
                            st.session_state.admin=True
                        st.session_state.seat = user_row["Seat"].values[0]
                        st.rerun()
                    else:
                        st.write("La password inserita è errata")
                else:
                    st.write("L'username inserito è errato")
                
            except Exception as e:
                st.error(f"Il server ha riscontrato un errore nel caricamento del database: {e}")



@st.dialog("AVVISO", dismissible=True)
def nonAdmin_dialog():
    st.write("""Non sei registrato come amministratore, questo vuol dire che puoi vedere unicamente il tuo posto.
    Se desideri vedere l'intera piantina accedi come amministratore o contatta l'assistenza""")


if st.session_state.logged==False:
    login_dialog()

else:
    studenti = [
    "Brusa", "Kalle", "Martina", "Dige", "Doyle", "Londino", "Carlo", "Arianna",
    "Sergio", "Mine", "Elena", "Veronica", "Francesca", "Cristina", "Iris",
    "Saita", "Signo", "Sammy", "Caterina", "Anna", "Peruta", "Zanoli", "Sciacca"
    ]


    lenght = len(studenti)
   

    curr_date = datetime.now() + timedelta(hours=11)

    seed_date = curr_date.strftime('%d/%m/%Y')

    random.seed(seed_date)
    random.shuffle(studenti)
    



    col_logo, _ = st.columns([1, 4]) 
    with col_logo:
        st.logo("big_brother_eye.png")

    st.subheader(f"Disposizione ufficiale del: {seed_date}")


    st.info(f"La disposizione si aggiorna automaticamente ogni giorno alle 16:00.")


    def desk(name, color="#e1f5fe"):
        st.markdown(f"""
            <div style="background-color: {color}; border: 2px solid #01579b; border-radius: 5px;
                padding: 10px; text-align: center; font-weight: bold; margin-bottom: 10px;
                color: #01579b; font-family: Arial;">
                {name}
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='background-color: #fb8c00; color: white; text-align: center; padding: 10px; font-weight: bold; border-radius: 5px; width: 200px; margin: 0 auto 30px auto;'>CATTEDRA</div>", unsafe_allow_html=True)
    
    
    if st.session_state.admin==False:
        if st.button("Come mai vedo i posti così?",type="primary"):
            nonAdmin_dialog()        
    col1, spacer1, col2, spacer2, col3 = st.columns([2, 1, 3, 1, 2])
    idx = 0


    
    
    
    with col1:
        st.write("**Fila Sinistra**")
        for r in range(3):
            c_sub1, c_sub2 = st.columns(2)
            with c_sub1:
                if st.session_state.admin == False:
                    if st.session_state.seat == studenti[idx]:
                        desk(studenti[idx])
                    else:
                        desk("****")
                else:
                    desk(studenti[idx])
                idx+=1
            with c_sub2: 
                if st.session_state.admin == False:
                    if st.session_state.seat == studenti[idx]:
                        desk(studenti[idx])
                    else:
                        desk("****")
                else:
                    desk(studenti[idx])
                idx+=1

    with col2:
        st.write("**Fila Centrale**")
        for r in range(3):
            c_sub1, c_sub2 = st.columns(2)
            with c_sub1: 
                if st.session_state.admin == False:
                    if st.session_state.seat == studenti[idx]:
                        desk(studenti[idx])
                    else:
                        desk("****")
                else:
                    desk(studenti[idx])
                idx+=1
            with c_sub2: 
                if st.session_state.admin == False:
                    if st.session_state.seat == studenti[idx]:
                        desk(studenti[idx])
                    else:
                        desk("****")
                else:
                    desk(studenti[idx])
                idx+=1
        c_sub1, c_sub2, c_sub3 = st.columns(3)
        for c in [c_sub1, c_sub2, c_sub3]:
            with c: 
                if st.session_state.admin == False:
                    if st.session_state.seat == studenti[idx]:
                        desk(studenti[idx])
                    else:
                        desk("****")
                else:
                    desk(studenti[idx])
                idx+=1

    with col3:
        st.write("**Fila Destra**")
        for r in range(4):
            c_sub1, c_sub2 = st.columns(2)
            if idx < lenght:
                with c_sub1: 
                    if st.session_state.admin == False:
                        if st.session_state.seat == studenti[idx]:
                            desk(studenti[idx])
                        else:
                            desk("****")
                    else:
                        desk(studenti[idx])
                    idx+=1
            if idx < lenght:
                with c_sub2: 
                    if st.session_state.admin == False:
                        if st.session_state.seat == studenti[idx]:
                            desk(studenti[idx])
                        else:
                            desk("****")
                    else:
                        desk(studenti[idx])
                    idx+=1

