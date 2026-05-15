'''
Uzdevums
Izveido programmu, kas:
 1. pajautā divus skaitļus,
 2. aprēķina to summu,
 3. izvada rezultātu.

Sagaidāmais rezultāts
 Ievadi pirmo skaitli:
 5
 Ievadi otro skaitli:
 7
 Summa ir 12.
'''
a = float(input("\nIevadi pirmo skaitli: "))
b = float(input("Ievadi otro skaitli: "))
summa = a + b

if summa.is_integer():
    print(f"\nSumma ir {summa:.0f}7.\n")
else:
    print(f"\nSumma ir {summa:.2f}\n")