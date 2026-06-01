import ttkbootstrap as tb
import ttkbootstrap.constants as tbs 

# from ttkbootstrap.constants import *

def apstradat_datus():
    ievaditais_vards = vards_entry.get()
    rezultats_label.config(text=f"Dati saglabāti! Sveiki, {ievaditais_vards}.")

def toggle_theme():
    # Tēmu pārslēgšana: pārslēgšanās no tumšas uz gaišu un otrādi
    current_theme = logs.style.theme_use()
    new_theme = "litera" if current_theme == "darkly" else "darkly"
    logs.style.theme_use(new_theme)
    # Pogas teksta atjaunināšana
    theme_btn.config(text=f"Pārslēgties uz {'tumšo' if new_theme == 'litera' else 'gaišo'} tēmu")

# 1. Izveidojiet logu ar noklusējuma tēmu “tumši”
width = 350
height = 250
logs = tb.Window(themename="darkly", title="Datu ievade", size=(width, height))
screen_width = logs.winfo_screenwidth()
screen_height = logs.winfo_screenheight()

# Aprēķiniet loga augšējā kreisā stūra koordinātas
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

# 3. Mēs izmantojam koordinātas: "platums x augstums + x + y"
logs.geometry(f"{width}x{height}+{x}+{y}")
logs.attributes('-topmost', True)
logs.resizable(False, False)

# 2. Izveidojiet konteineru elementiem (kārtīguma labad)
frame = tb.Frame(logs, padding=20)
frame.pack(fill=tbs.BOTH, expand=tbs.YES)

# Saskarnes elementi
tb.Label(frame, text="Ievadiet vārdu:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)

vards_entry = tb.Entry(frame, width=20, font=("Arial", 14))
vards_entry.grid(row=0, column=1, padx=10, pady=10)

apstrades_poga = tb.Button(frame, text="Apstrādāt datus", command=apstradat_datus, bootstyle="success-outline")
apstrades_poga.grid(row=1, column=0, columnspan=2, pady=15)

rezultats_label = tb.Label(frame, text="", font=("Arial", 18, "bold"), bootstyle="info")
rezultats_label.grid(row=2, column=0, columnspan=2, pady=10)

# Poga Mainīt tēmu
theme_btn = tb.Button(frame, text="Pārslēgties uz gaišo tēmu", command=toggle_theme, bootstyle="secondary")
theme_btn.grid(row=3, column=0, columnspan=2, pady=10)

logs.mainloop()