import tkinter as tk

def parbaudit_paroli():
    parole = parole_entry.get()
    atkartota_parole = atkartota_entry.get()
    
    kludas = []
    a = len(parole)
    spec_simboli = "!@#$%^&*()_+-=[]{}|;':\",./<>?"

    # 1) и 2) Проверка длины
    if a < 8:
        kludas.append("Пароль слишком короткий (минимум 8 символов).")
    elif a > 25:
        kludas.append("Пароль слишком длинный (максимум 25 символов).")

    # 3) Проверка пробелов, цифр и строчных букв
    if " " in parole:
        kludas.append("Пароль не должен содержать пробелы.")
    if not any(c.isdigit() for c in parole):
        kludas.append("В пароле должна присутствовать как минимум одна цифра.")
    if not any(c.islower() for c in parole):
        kludas.append("В пароле должна присутствовать как минимум одна строчная буква.")

    # 4) Проверка на латиницу
    if not parole.isascii():
        kludas.append("Используйте для ввода только латиницу.")

    # 5) Проверка заглавных букв
    if not any(c.isupper() for c in parole):
        kludas.append("В пароле нужна как минимум одна заглавная буква.")

    # 6) Проверка спецсимволов
    if not any(not c.isalnum() for c in parole):
        kludas.append(f"В пароле должен быть минимум один спецсимвол из: {spec_simboli}")

    # Дополнительно: Проверка совпадения паролей
    if parole != atkartota_parole:
        kludas.append("Пароли не совпадают!")

    # Вывод результатов прямо в окно (используя Label)
    if len(kludas) == 0:
        pazinojums_label.config(text="Пароль принят!\nОкно закроется через 2 секунды...", fg="#4CAF50")
        root.after(2000, root.destroy)
    else:
        # Объединяем все ошибки в один текст с переносом строки (\n)
        kludu_teksts = "Обнаруженные ошибки:\n" + "\n".join([f"- {k}" for k in kludas])
        pazinojums_label.config(text=kludu_teksts, fg="#FF5252")

# --- Структура окна ---
root = tk.Tk()
root.title("Регистрация - Проверка пароля")
root.geometry("500x450")

# 1. Поле ввода пароля
tk.Label(root, text="Введите пароль:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=5)
parole_entry = tk.Entry(root, show="*", font=("Arial", 11), width=40)
parole_entry.pack(padx=20)

# 2. Повторный ввод пароля
tk.Label(root, text="Повторите пароль:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=5)
atkartota_entry = tk.Entry(root, show="*", font=("Arial", 11), width=40)
atkartota_entry.pack(padx=20)

# Кнопка проверки (с фиксированным цветом текста 'black', чтобы Dark Mode его не скрывал)
poga = tk.Button(root, text="Регистрация", command=parbaudit_paroli, 
                 bg="#4CAF50", fg="black", activebackground="#45a049", font=("Arial", 10, "bold"))
poga.pack(pady=20)

# 3. Место для вывода сообщений об ошибках (обычный Label прямо на фоне окна)
pazinojums_label = tk.Label(root, text="", font=("Arial", 10), justify="left", anchor="w")
pazinojums_label.pack(fill="x", padx=20, pady=10)

root.mainloop()

# Asdf123!