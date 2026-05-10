cities = ["Riga", "Vilnius", "Tallinn", "Moscow", "Warsaw"]
cities.append("Berlin")
print(cities)
# 1. Viena elementa izvēle (atceramies, ka skaitīšana sākas no nulles!)
#    (Выбор одного элемента — помним, что счёт начинается с нуля!)
print(f"Pirmā pilsēta: {cities[0]}") 
print(f"Trešā pilsēta: {cities[2]}")
print(f"Pēdējā pilsēta: {cities[-1]}") # Mīnus 1 vienmēr ņem pēdējo elementu!
# (Минус 1 всегда берёт самый последний элемент!)
print("========================================================")
# 2. Šķēles (Slicing) — diapazona izvēle [sākums : beigas]
#    (Срезы — выбор диапазона [начало : конец])
# SVARĪGI: Beigas netiek iekļautas atlasē!
# (ВАЖНО: Конец не включается в выборку!)
print(f"Pirmās trīs pilsētas: {cities[:3]}")      # No sākuma līdz 3. (neiekļaujot to)
# (Первые три города: от начала до 3-го, не включая его)
print(f"Pilsētas no 2. līdz 4.: {cities[1:4]}")  # Indeksi 1, 2, 3
# (Города со 2-го по 4-й: индексы 1, 2, 3)
print(f"Viss pēc otrās pilsētas: {cities[2:]}")
# (Всё после второго города)
print("========================================================")
# 3. Soļi (Step) — kad nevajag ņemt visu pēc kārtas
#    (Шаги — когда не нужно брать всё подряд)
print(f"I katra otrā pilsēta: {cities[::2]}")   # Visu saraksts ar soli 2
# (Каждый второй город: весь список с шагом 2)
print(f"Saraksts no gala līdz sākumam: {cities[::-1]}") # Python maģija reversēšanai
# (Список задом наперёд: магия Python для реверса)

cities.insert(1, "London")  # Ievietojam "London" pozīcijā ar indeksu 1
# (Вставляем "London" на позицию с индексом 1)
cities.insert(3, "Paris")   # Ievietojam "Paris" pozīcijā ar indeksu 3
# (Вставляем "Paris" на позицию с индексом 3)
cities.insert(1, "Berlin")  # Ievietojam "Berlin" pozīcijā ar indeksu 1
# (Вставляем "Berlin" на позицию с индексом 1)

print(cities)
print(cities[2], cities[4])