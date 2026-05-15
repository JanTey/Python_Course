'''
Uzdevums
Programmai jāizvada lietotāja vārds, bet tā to nedara pareizi.
Salabo kodu:
    vards = input("Kā tevi sauc? ")       # Anna
    print(f"Sveiks, vards!") --- nepareizi, jo vārds tiek izvadīts kā teksts "vards", nevis mainīgā vērtība
    print(f"Sveika, {vards}!")     # Sveika, Anna!
'''

vards = input("Kā tevi sauc? ")
if vards[-1].lower() == "a" or vards[-1].lower() == "e":
    print(f"Sveika, {vards}!")
else:
    print(f"Sveiks, {vards}!")