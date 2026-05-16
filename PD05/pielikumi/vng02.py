'''
Uzdevums
Izveido programmu, kas:
1. palūdz ievadīt vecumu;
2. pārbauda, vai vecums ir diapazonā no 0 līdz 120;
3. izvada:
“Vecums izskatās reāls”
vai
“Ievadīts nereāls vecums”.

Sagaidāmais rezultāts
Ievadi vecumu:
25
Vecums izskatās reāls.
'''

try:
    vecums = int(input("Ievadi vecumu: "))
    
    if vecums > 0 and vecums < 120:
        print(f"\nVecums izskatās reāls.\n")
    else:
        print(f"\nIevadīts nereāls vecums.\n")
        
except ValueError:
    print("\nKļūda: Ievadītais teksts nav skaitlis!\n")