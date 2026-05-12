import tkinter as tk
from tkinter import messagebox, simpledialog

# Paslēpjam galveno tukšo logu (Прячем основное окно)
root = tk.Tk()
root.withdraw()

# 1. Nolasa pilsētas (Загружаем данные)
try:
    with open("/Users/jante/Documents/Python_Course/cities1.txt", "r", encoding="utf-8") as file:
        cities = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    messagebox.showerror("Kļūda", "Fails cities.txt netika atrasts!")
    exit()

# 2. Uzsāk ciklu (Запускаем цикл)
while True:
    # Grafisks logs ievadei (Графическое окно для ввода)
    user_choice = simpledialog.askstring("Ceļojums", "Uz kuru pilsētu Jūs vēlaties doties?\n(Ievadiet 'N', lai izietu):")

    # Ja lietotājs nospiež 'Cancel' vai ievada 'N'
    if user_choice is None or user_choice.upper() == "N":
        messagebox.showinfo("Info", "Programma pabeigta. Jauku ceļojumu!")
        break

    found = False
    for index, city in enumerate(cities):
        if user_choice.lower() == city.lower():
            messagebox.showinfo("Atrasts!", f"Pilsēta {city} ir sarakstā ar numuru {index + 1}!")
            found = True
            break
    
    if not found:
        messagebox.showwarning("Nav atrasts", f"Pilsēta '{user_choice}' mūsu sarakstā nav.")