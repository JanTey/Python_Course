import tkinter as tk
from tkinter import messagebox


def aprekinat_summu():
    try:
        # Iegūstam datus no laukiem un pārvēršam par float
        skaitlis1 = float(entry1.get())
        skaitlis2 = float(entry2.get())

        # Veicam aprēķinu
        rezultats = skaitlis1 + skaitlis2

        # Atjauninām etiķeti ar rezultātu, izmantojot f-string
        result_label.config(text=f"Summa divu skaitļu ir: {rezultats:.2f}")
    except ValueError:
        # Ja ievadīts teksts, nevis skaitlis
        messagebox.showerror("Kļūda", "Lūdzu, ievadiet tikai skaitļus!")


# Izveidojam galveno logu
root = tk.Tk()
root.title("Summas aprēķins")
root.geometry("300x250")

# Pirmais skaitlis
tk.Label(root, text="Ievadiet pirmo skaitli:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# Otrais skaitlis (novietots zem pirmā)
tk.Label(root, text="Ievadiet otro skaitli:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Poga aprēķināšanai
btn = tk.Button(root, text="Aprēķināt", command=aprekinat_summu)
btn.pack(pady=10)

# Vieta rezultātam
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
