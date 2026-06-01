import os
import sqlite3
import hashlib
import ttkbootstrap as tb
from tkinter import messagebox
from ttkbootstrap.constants import *

# --- ПУТИ ---
basedir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(basedir, "lietotaji.db")
faila_cels = os.path.join(basedir, "dzivnieki.txt")

# --- БАЗА ДАННЫХ И ХЕШИРОВАНИЕ ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (username TEXT PRIMARY KEY, password_hash TEXT)''')
    conn.commit()
    conn.close()

# --- IEEJAS LOĢIKA ---
def check_login():
    username = user_entry.get()
    password = password_entry.get()
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result and result[0] == hash_password(password):
        login_window.destroy()
        tb.Style.instance = None 
        start_main_app()
    else:
        messagebox.showerror("Kļūda", "Nepareizs lietotājvārds vai parole!", parent=login_window)

def register_user():
    username = user_entry.get()
    password = password_entry.get()
    if not username or not password:
        messagebox.showwarning("Kļūda", "Aizpildiet visus laukus!", parent=login_window)
        return
        
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users VALUES (?, ?)", (username, hash_password(password)))
        conn.commit()
        conn.close()
        messagebox.showinfo("Veiksmīgi", "Reģistrācija veiksmīga!", parent=login_window)
    except sqlite3.IntegrityError:
        messagebox.showerror("Kļūda", "Lietotājs jau eksistē!", parent=login_window)

# --- MAIN PROGRAM ---
def start_main_app():
    logs = tb.Window(themename="darkly", title="Dzīvnieku reģistrs")
    
    # Centrēšana
    width, height = 300, 350
    sw, sh = logs.winfo_screenwidth(), logs.winfo_screenheight()
    x = (sw // 2) - (width // 2)
    y = (sh // 2) - (height // 2)
    logs.geometry(f"{width}x{height}+{x}+{y}")

    # Ligzdotas funkcijas
    def saglabat_datus():
        s, v, vc = suga_entry.get(), vards_entry.get(), vecums_entry.get()
        if not s or not v or not vc:
            messagebox.showwarning("Kļūda", "Aizpildiet visus laukus!", parent=logs)
            return
        with open(faila_cels, "a", encoding="utf-8") as f:
            f.write(f"{s}|{v}|{vc}\n")
        suga_entry.delete(0, END); vards_entry.delete(0, END); vecums_entry.delete(0, END)
        messagebox.showinfo("Veiksmīgi", "Dati ir saglabāti!", parent=logs)

    def parradit_sarakstu():
        list_window = tb.Toplevel(logs)
        list_window.title("Dzīvnieku saraksts")
        list_window.geometry("500x300")

        # Treeview
        tree = tb.Treeview(list_window, columns=("id", "suga", "vards", "vecums"), show="headings")
        
        column_configs = {
            "id": {"text": "Id", "width": 50},
            "suga": {"text": "Suga", "width": 140},
            "vards": {"text": "Vards", "width": 140},
            "vecums": {"text": "Vecums", "width": 80}
        }

        for col, config in column_configs.items():
            # anchor=W izlīdzina virsrakstu pa kreisi
            tree.heading(col, text=config["text"], anchor=W)
            
            # anchor=W izlīdzina datus šūnās pa kreiso malu
            tree.column(col, width=config["width"], minwidth=config["width"], anchor=W, stretch=YES)

        tree.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        if os.path.exists(faila_cels):
            with open(faila_cels, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    if "|" in line: 
                        tree.insert("", END, values=(i, *line.strip().split("|")))

    def toggle_theme():
        current_theme = logs.style.theme_use()
        new_theme = "litera" if current_theme == "darkly" else "darkly"
        logs.style.theme_use(new_theme)
        theme_btn.config(text=f"Tēma: {'Tumšā' if new_theme == 'darkly' else 'Gaišā'}")

    # Интерфейс
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

    tb.Button(frame, text="Saglabāt", command=saglabat_datus, bootstyle="success").grid(row=3, column=0, columnspan=2, pady=10, sticky="e", padx=0)
    tb.Button(frame, text="Parādīt sarakstu", command=parradit_sarakstu, bootstyle="info").grid(row=4, column=0, columnspan=2, sticky="e", padx=0)
    theme_btn = tb.Button(frame, text="Tēma: Tumšā", command=toggle_theme, bootstyle="secondary-outline")
    theme_btn.grid(row=5, column=0, columnspan=2, pady=10, sticky="e", padx=0)

    # Fokusēt un atvērt galveno logu priekšplānā
    suga_entry.focus_set()
    logs.lift()
    logs.focus_force()

    logs.mainloop()

# --- СТАРТ ---
init_db()

# Izveidojiet pieteikšanās logu bez fiksēta izmēra dizainerā
login_window = tb.Window(themename="darkly", title="Ielogoties")

# Autorizācijas loga centrēšana
width, height = 300, 250
sw, sh = login_window.winfo_screenwidth(), login_window.winfo_screenheight()
x = (sw // 2) - (width // 2)
y = (sh // 2) - (height // 2)
login_window.geometry(f"{width}x{height}+{x}+{y}")

frame = tb.Frame(login_window, padding=20)
frame.pack(fill=BOTH, expand=YES)

tb.Label(frame, text="Lietotājvārds:").pack()
user_entry = tb.Entry(frame)
user_entry.pack()

tb.Label(frame, text="Parole:").pack()
password_entry = tb.Entry(frame, show="*")
password_entry.pack()

btn_frame = tb.Frame(frame)
btn_frame.pack(pady=10)
tb.Button(btn_frame, text="Ieiet", command=check_login, bootstyle="success").pack(side=LEFT, padx=5)
tb.Button(btn_frame, text="Reģistrēt", command=register_user, bootstyle="info").pack(side=LEFT, padx=5)

# Fokusa iestatīšana uz pieteikšanās ievades lauku
user_entry.focus_set()

# Izvietot logu priekšplānā virs citām palaistajām lietotnēm
login_window.lift()
login_window.focus_force()

login_window.mainloop()