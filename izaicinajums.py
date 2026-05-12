import tkinter as tk
from tkinter import messagebox
import os

# Paslēpjam galveno tukšo logu (Прячем основное окно)
root = tk.Tk()
root.withdraw()

messagebox.showinfo("Mani sauc Žanis", "Šodien es sāku programmēt Python!")

root.destroy()
