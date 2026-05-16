'''
Uzdevums
Izveido programmu, kas:
1. palūdz ievadīt divus skaitļus;
2. salīdzina tos;
3. izvada:
kurš skaitlis ir lielāks;
vai skaitļi ir vienādi.
Sagaidāmais rezultāts
Ievadi pirmo skaitli:
10
Ievadi otro skaitli:
7
Pirmais skaitlis ir lielāks.
'''

skaitlis1 = int(input("\nIevadi pirmo skaitli: "))
skaitlis2 = int(input("Ievadi otro skaitli: "))

if skaitlis1 > skaitlis2:
    print(f"\nPirmais skaitlis ({skaitlis1}) ir lielāks par otro ({skaitlis2}).\n")
elif skaitlis2 > skaitlis1:
    print(f"\nOtrais skaitlis ({skaitlis2}) ir lielāks par pirmo ({skaitlis1}).\n")
else:
    print(f"\nAbi skaitļi ir vienādi ({skaitlis1}).\n")