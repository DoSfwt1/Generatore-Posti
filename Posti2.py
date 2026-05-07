import tkinter as tk
import random
from datetime import datetime, timedelta

# Inizializza la data con il giorno corrente (OGGI)
data_simulata = datetime.now()

def genera_disposizione():
    global data_simulata
    
    # Lista dei 23 studenti
    studenti = [
        "Brusa", "Kalle", "Martina", "Dige", "Doyle", "Londino", "Carlo", "Arianna",
        "Sergio", "Mine", "Elena", "Veronica", "Francesca", "Cristina", "Iris",
        "Saita", "Signo", "Sammy", "Caterina", "Anna", "Peruta", "Zanoli", "Sciacca"
    ]
    
    random.shuffle(studenti)
    canvas.delete("all")
    
    # Mostra la data attuale della simulazione e poi incrementa di 1 giorno per il prossimo click
    label_data.config(text=f"Disposizione del: {data_simulata.strftime('%d/%m/%Y')}")
    data_simulata += timedelta(days=1)
    
    w_banco, h_banco = 95, 45
    spazio_y = 25
    idx = 0

    def disegna(x, y, nome, colore="#e1f5fe"):
        canvas.create_rectangle(x, y, x + w_banco, y + h_banco, fill=colore, outline="#01579b", width=2)
        canvas.create_text(x + w_banco/2, y + h_banco/2, text=nome, font=("Arial", 9, "bold"), width=w_banco-5)

    # Coordinate X per le tre file: Sinistra, Centro, Destra
    x_pos = [50, 320, 600]

    # --- FILA SINISTRA (6 posti: 3 coppie) ---
    for r in range(3):
        for p in range(2):
            disegna(x_pos[0] + (p * (w_banco + 5)), 60 + (r * (h_banco + spazio_y)), studenti[idx])
            idx += 1

    # --- FILA CENTRALE (9 posti: 3 coppie + 1 terzetto finale) ---
    for r in range(3):
        for p in range(2):
            disegna(x_pos[1] + (p * (w_banco + 5)), 60 + (r * (h_banco + spazio_y)), studenti[idx])
            idx += 1
    # Terzetto finale (Fila centrale, quarta riga)
    for p in range(3):
        offset_x = (x_pos[1] - 50) + (p * (w_banco + 5))
        disegna(offset_x, 60 + (3 * (h_banco + spazio_y)), studenti[idx], colore="#fff9c4")
        idx += 1

    # --- FILA DESTRA (8 posti: 4 coppie) ---
    for r in range(4):
        for p in range(2):
            if idx < len(studenti):
                disegna(x_pos[2] + (p * (w_banco + 5)), 60 + (r * (h_banco + spazio_y)), studenti[idx])
                idx += 1

    # Cattedra
    canvas.create_rectangle(340, 5, 540, 35, fill="#fb8c00", outline="black")
    canvas.create_text(440, 20, text="CATTEDRA", fill="white", font=("Arial", 10, "bold"))

# Setup Finestra
root = tk.Tk()
root.title("Generatore Posti Classe - Simulatore Giornaliero")
root.geometry("900x600")

label_data = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#333")
label_data.pack(pady=10)

canvas = tk.Canvas(root, width=880, height=420, bg="white", highlightthickness=1)
canvas.pack(pady=10)

btn = tk.Button(root, text="🔄 GENERA PER IL GIORNO SUCCESSIVO", command=genera_disposizione, 
                font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10)
btn.pack()

# Avvia con la data di oggi al primo colpo
genera_disposizione()

root.mainloop()
