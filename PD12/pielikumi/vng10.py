"""
Uzdevums
Izveido programmu, kas failā zurnals.txt pieraksta notikumu.
Programma prasa:
Ievadi notikumu:
Piemēram:
Serveris pārbaudīts
Pēc tam programma:
1. pieraksta notikumu failā;
2. nolasa visu žurnālu;
3. izvada to ekrānā.
Sagaidāmais rezultāts
Ievadi notikumu:
Serveris pārbaudīts

Žurnāls:

Programma palaista
Serveris pārbaudīts
"""

notikums = input("\nIevadi notikumu: \n")
with open("PD12/zurnals.txt", "a", encoding="utf-8") as fails:
    fails.write(notikums + "\n")
with open("PD12/zurnals.txt", "r", encoding="utf-8") as fails:
    print("\nŽurnāls:\n\n" + fails.read())
