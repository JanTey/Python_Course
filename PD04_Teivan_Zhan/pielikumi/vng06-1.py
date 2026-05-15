'''
Uzdevums: Ūdens vārīšanās temperatūras pārbaude

Mērķis:
Izveidot programmu, kas simulē temperatūras kontroli, izmantojot zarošanās loģiku (if-elif-else) un vairāku nosacījumu pārbaudi vienā rindā (or).

Uzdevuma nosacījumi:

Lietotājs ievada temperatūru kā decimālskaitli (float).

Programma pārbauda, vai ievadītā vērtība ir loģiskajās robežās (no 0 līdz 100 grādiem). Ja nē — izvada kļūdas paziņojumu.

Ja temperatūra ir precīzi 100 grādi, programma paziņo, ka ūdens vārās.

Ja temperatūra ir zem 100 grādiem, programma paziņo, ka vārīšanās vēl nav sākusies.

Sagaidāmie rezultāti (Expected Results)

1. scenārijs (Kļūda):

Ievadiet ūdens temperatūru (0-100 Celsija grādos): 105
Kļūda: Temperatūra 105.0°C nav iespējama šādos apstākļos!


2. scenārijs (Vārīšanās):

Ievadiet ūdens temperatūru (0-100 Celsija grādos): 100
Ūdens vārās! Temperatūra ir sasniegusi 100.0°C.


3. scenārijs (Zema temperatūra):

Ievadiet ūdens temperatūru (0-100 Celsija grādos): 75.5
Ūdens vēl nevārās. Pašreizējā temperatūra: 75.5°C.
'''
# Programma, kas pārbauda, vai ūdens ir sasniedzis vārīšanās temperatūru

# Lietotājs ievada pašreizējo temperatūru
temperatura = float(input("\nIevadiet ūdens temperatūru (0-100 Celsija grādos): "))


if temperatura > 100 or temperatura < 0:
    print(f"\nKļūda: Temperatūra {temperatura}°C nav iespējama šādos apstākļos!\n")
elif temperatura == 100:
    print(f"\nŪdens vārās! Temperatūra ir sasniegusi {temperatura}°C.\n")
else:
    print(f"\nŪdens vēl nevārās. Pašreizējā temperatūra: {temperatura}°C.\n")