import os
import sqlite3        # Для работы с базой данных
import hashlib
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox, ttk

# Dzīvnieku klase (nemainīga)
class Dzivnieks:
    def __init__(self, suga, vards, vecums):
        self.suga = suga
        self.vards = vards
        self.vecums = vecums
        
    def formatet_ierakstam(self):
        return f"{self.suga}|{self.vards}|{self.vecums}\n"

# Tēmas pārslēgšanas funkcija (PIEVIENOTA)
def toggle_theme():
    # Tēmu pārslēgšana: pārslēgšanās no tumšas uz gaišu un otrādi
    current_theme = logs.style.theme_use()
    new_theme = "litera" if current_theme == "darkly" else "darkly"
    logs.style.theme_use(new_theme)
    # Pogas teksta atjaunināšana
    theme_btn.config(text=f"Pārslēgties uz {'tumšo' if new_theme == 'litera' else 'gaišo'} tēmu")


# Ceļš uz mapi, kurā atrodas programma
skripta_mape = os.path.dirname(os.path.abspath(__file__))
# Pilna faila ceļa veidošana
faila_cels = os.path.join(skripta_mape, "dzivnieki.txt")
# Funkcija datu saglabāšanai
def saglabat_datus():
    # Nolasām datus no ievades laukiem
    s = suga_entry.get()
    v = vards_entry.get()
    vc = vecums_entry.get()
    
    if not s or not v or not vc:
        messagebox.showwarning("Kļūda", "Lūdzu, aizpildiet visus laukus!", parent=logs)
        return

    dz = Dzivnieks(s, v, vc)
    
    # Ierakstām failā
    with open(faila_cels, "a", encoding="utf-8") as f:
        f.write(dz.formatet_ierakstam())
    
    # Iztīrām laukus
    suga_entry.delete(0, END)
    vards_entry.delete(0, END)
    vecums_entry.delete(0, END)
    messagebox.showinfo("Veiksmīgi", "Dati ir saglabāti!", parent=logs)

# Funkcija saraksta parādīšanai tabulā
def parradit_sarakstu():
    list_window = tb.Toplevel(logs)
    list_window.title("Dzīvnieku saraksts")
    list_window.geometry("400x300")

    # Tabulas (Treeview) izveide
    columns = ("id", "suga", "vards", "vecums")
    tree = ttk.Treeview(list_window, columns=columns, show="headings")
    
    tree.heading("id", text="№")
    tree.heading("suga", text="Suga")
    tree.heading("vards", text="Vārds")
    tree.heading("vecums", text="Vecums")
    
    
    tree.column("id", width=30)
    tree.column("suga", width=100)
    tree.column("vards", width=100)
    tree.column("vecums", width=50)
    
    tree.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    # Nolasa datus no faila
    try:
        with open(faila_cels, "r", encoding="utf-8") as f:
            i = 1
            for line in f:
                if "|" in line:
                    data = line.strip().split("|")
                    tree.insert("", END, values=(i, *data))
                    i += 1
    except FileNotFoundError:
        pass

# Galvenais logs
width = 300
height = 300 
logs = tb.Window(themename="darkly", title="Dzīvnieku reģistrs", size=(width, height))
logs.focus_force()
screen_width = logs.winfo_screenwidth()
screen_height = logs.winfo_screenheight()

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

# 3. Mēs izmantojam koordinātas: "platums x augstums + x + y"
logs.geometry(f"{width}x{height}+{x}+{y}")
# logs.attributes('-topmost', True)
logs.resizable(False, False)

# Interfeiss
frame = tb.Frame(logs, padding=20)
frame.pack(fill=BOTH, expand=YES)

tb.Label(frame, text="Suga:").grid(row=0, column=0, pady=5)
suga_entry = tb.Entry(frame)
suga_entry.grid(row=0, column=1, pady=5)

tb.Label(frame, text="Vārds:").grid(row=1, column=0, pady=5)
vards_entry = tb.Entry(frame)
vards_entry.grid(row=1, column=1, pady=5)

tb.Label(frame, text="Vecums:").grid(row=2, column=0, pady=5)
vecums_entry = tb.Entry(frame)
vecums_entry.grid(row=2, column=1, pady=5)

tb.Button(frame, text="Saglabāt", command=saglabat_datus, bootstyle="success").grid(row=3, column=0, columnspan=2, pady=10)
tb.Button(frame, text="Parādīt sarakstu", command=parradit_sarakstu, bootstyle="info").grid(row=4, column=0, columnspan=2)

# Tēmas pārslēgšanas poga
theme_btn = tb.Button(frame, text="Tēma: Tumšā", command=toggle_theme, bootstyle="secondary-outline")
theme_btn.grid(row=5, column=0, columnspan=2, pady=10)

logs.mainloop()