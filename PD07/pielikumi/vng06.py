'''
Uzdevums
Izveido programmu, kas izvada skaitļa 
7 reizināšanas tabulu.
Sagaidāmais rezultāts
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
'''

print()
skaitlis = 7
for i in range(1, 11):
    print(f"{i} x {skaitlis} = {i * skaitlis}")
print()    
    
'''
i = 1
skaitlis = 7
while i < 11:
    print(f"{i} x {skaitlis} = {i * skaitlis}")
    i += 1
'''