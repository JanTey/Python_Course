'''
Uzdevums
Izveido programmu, kas pajautā skaitli un pārbauda, vai tas ir pozitīvs.
Prasības
Ja skaitlis ir lielāks par 0, izvada:
Skaitlis ir pozitīvs.
Citādi izvada:
Skaitlis nav pozitīvs.
'''

skaitlis = int(input("\nIevadi skaitli: "))
if skaitlis > 0:
    print("\nSkaitlis ir pozitīvs.\n")
else:
    print("\nSkaitlis nav pozitīvs.\n")