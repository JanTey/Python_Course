cities = ["Riga", "Berlin", "London", "Vilnius", "Paris", "Tallinn", "Warsaw"]
# Cikls iet cauri visam pilsētu sarakstam (Цикл проходит через весь список городов)
for city in cities:
    # Pārbaudām, vai pilsētas nosaukuma garums ir lielāks par 5 simboliem
    # (Проверяем, больше ли длина названия города 5 символов)

    """

    == — Равно
    != — Не равно
    > / < — Больше / Меньше
    >= / <= — Больше или равно / Меньше или равно

    """

    if len(city) > 5:
        # Ja nosacījums ir patiess, izvadām šo frāzi (Если условие истинно, выводим эту фразу)
        # (Я хочу поехать в {city})
        print(            f"Es gribu aizbraukt uz {city.upper().replace('A', 'a').replace('N', 'n')}"
        )
    else:
        # Ja nosaukums ir īss, vienkārši parādām pilsētu (Если название короткое, просто показываем город)
        print(f"Pilsēta: {city}")  # (Город: {city})

print("========================================================")

# enumerate dod mums vienlaikus gan INDEKSU (numuru), gan pašu ELEMENTU
# (enumerate даёт нам одновременно и ИНДЕКС (номер), и сам ЭЛЕМЕНТ)
"""
Piemērs bez enumerate — tikai pilsētas nosaukumi (Пример без enumerate — только названия городов)
enumerate(cities): Это «улучшайзер» для цикла. Без него ты получаешь просто название города. 
С ним ты получаешь пару: (0, 'Riga'), (1, 'Berlin') и так далее.
"""
for index, city in enumerate(cities):
    if index % 2 == 0:  # (index % 2 != 0) - проверка нечетности
        # Pārbaudām, vai indekss ir pāra skaitlis (Проверяем, является ли индекс чётным числом)

        # (стоит на чётной позиции)
        print(f"{index+1}. [{index}] {city} — atrodas pāra pozīcijā")
    else:
        # (стоит на нечётной позиции)
        print(f"{index+1}. [{index}] {city} — atrodas nepāra pozīcijā")
