import tkinter as tk
from tkinter import messagebox

vards = "Žanis"
uzvards = "Teivāns"
print(f"Labrīt, {vards} {uzvards}!")

# Paslēpjam galveno tukšo logu (Прячем основное окно)
root = tk.Tk()
root.withdraw()

messagebox.showinfo(f"Labrīt", f"{vards} {uzvards}!")

root.destroy()
