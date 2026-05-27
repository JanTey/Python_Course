"""
Uzdevums
Izveido programmu.
Prasības:
prasa skaitli;
teksts neizraisa sarkanu kļūdu.
Piemērs:
Ievadi:
abc
Ievadi skaitli.
"""

while True:
    try:
        skaitlis = int(input("\nIevadi skaitli: "))
        print()
        break
    except ValueError:
        print("Kļūda! Lūdzu, ievadi veselu skaitli.")   