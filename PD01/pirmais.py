import tkinter as tk
from tkinter import messagebox

print("man izdevās!")

# Paslēpjam galveno tukšo logu (Прячем основное окно)
root = tk.Tk()
root.withdraw()

messagebox.showinfo("Mani sauc Žanis", "Šodien es sāku programmēt Python!")

root.destroy()
