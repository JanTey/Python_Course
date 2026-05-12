
# 1. Метод file.readlines()
"""
=========================================================
        Он превращает файл в список (list) отдельных строк.
        Python должен как-то сохранить информацию о том, где заканчивалась одна строка и
        начиналась другая. Поэтому он оставляет символ \n внутри каждой строки.
        В памяти это выглядит так: ["Rīga\n", "Ventspils\n", "Daugavpils\n"]
        Если ты начнешь сравнивать if "Rīga" == city, то "Rīga" (из ввода пользователя) не совпадет
        с "Rīga\n" (из списка).
=========================================================
"""

# Faila atvēršana lasīšanas režīmā (Открытие файла в режиме чтения)
# Замените путь ниже на полный путь к файлу из вашей системы
with open("pielikumi//cities1.txt", "r", encoding="utf-8") as file:
    
    # Faila satura pārvēršana sarakstā (Превращение содержимого файла в список)
    cities_from_file = [line.strip() for line in file.readlines()]

# Tagad mēs varam izmantot ciklu (Теперь мы можем использовать цикл)
for city in cities_from_file:
    # .strip() noņem liekas atstarpes un jaunas rindiņas simbolus
    # (.strip() убирает лишние пробелы и символы переноса строки)
    print(city.upper())
    print(city.lower())
    print("========================================================")

    """
    ========================================================
            .lower()	Все буквы маленькие
            .upper()	Все буквы большие
            .title()	Каждое слово с большой буквы
            .capitalize()	Первый символ заглавный, остальные маленькие
            .strip()	Удаляет пробелы в начале и в конце строки
            .replace("a", "A")	Заменяет все "a" на "A"
            .split(",")	Разбивает строку на части по запятой и возвращает список    
    ========================================================
    """


# 2. Метод file.read()
# =================================================================================
# =================================================================================

with open("pielikumi//cities1.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("========================================================")
    print(content)

"""
        Метод file.read()
        Он считывает весь файл как одну огромную строку.
        Когда ты делаешь print(content), Python просто выводит этот длинный текст на экран.
        Символы переноса строки (\n), которые есть в файле, работают как команды для консоли: 
        «перейди на новую строку».
        Результат: Ты видишь красивый столбик, потому что консоль послушно переносит текст там, 
        где в файле стоят невидимые метки конца строки.
"""
# =================================================================================
# =================================================================================


# 3. # Uzsāk bezgalīgu ciklu (Запускает бесконечный цикл)
while True:
    # Pajautā lietotājam pilsētu (Спрашивает у пользователя город)
    user_choice = input(
        "\nUz kuru pilsētu Jūs vēlaties doties? (ievadiet 'N', lai izietu): "
    )

    # Pārbauda, vai lietotājs vēlas pārtraukt (Проверяет, хочет ли пользователь выйти)
    if user_choice.upper() == "N":
        print("Programma ir pabeigta. Jauku ceļojumu!")  # Программа завершена. Приятного путешествия!
        #messagebox.showinfo("Info", "Programma pabeigta. Jauku ceļojumu!") # Uzraksts logā
        break  # Pārtrauc ciklu (Прерывает цикл)

    found = False  # Mainīgais, kas glabā informāciju, vai pilsēta ir atrasta (Флаг поиска - Переменная, хранящая информацию о том, найден ли город)

    # Meklē pilsētu sarakstā (Ищет город в списке)
    for index, city in enumerate(cities_from_file):
        if user_choice.lower() == city.lower():
            print(f"Jā, pilsēta {city} ir sarakstā ar numuru {index + 1}!")
            #messagebox.showinfo("Atrasts!", f"Pilsēta {city} ir sarakstā ar numuru {index + 1}!")
            found = True
            break

    # Ja pilsēta netika atrasta (Если город не был найден)
    if not found:
        # Brīdinājuma logs (Окно предупреждения)
        print("Diemžēl šādas pilsētas mūsu sarakstā nav.")
        #messagebox.showwarning("Kļūda", "Diemžēl šādas pilsētas nav sarakstā.")
