'''Uzdevums
Izveido programmu, kas:
1. pajautā vienas kafijas cenu,
2. pajautā izdzerto kafiju skaitu,
3. aprēķina kopējās izmaksas.
Sagaidāmais rezultāts
Cik maksā viena kafija?
2.5
Cik kafijas izdzer mēnesī?
30
Tu mēnesī kafijai iztērē 75.0 EUR
'''
cena = float(input("Cik maksā viena kafija? "))
skaits = int(input("Cik kafijas izdzer mēnesī? "))
kopējās_izmaksas = cena * skaits
print(f"Tu mēnesī kafijai iztērē {kopējās_izmaksas} EUR.")