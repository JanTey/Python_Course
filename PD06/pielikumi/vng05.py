'''
Uzdevums
Programma lūdz ievadīt skaitli un izvada tā reizināšanas tabulu no 1 līdz 10.
Sagaidāmais rezultāts
Ievadi skaitli: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
'''

x = int(input("\nIevadi skaitli: "))
print()
for i in range(1,11):
    y = x * i
    print(f"{x} x {i} = {y}")
print()    