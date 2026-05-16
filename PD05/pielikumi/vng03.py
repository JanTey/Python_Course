'''
Uzdevums
Izveido programmu, kas:
1. palūdz ievadīt paroli;
2. pārbauda, vai parole satur vismaz 8 simbolus;
3. izvada:
“Parole der”
vai
“Parole ir pārāk īsa”.
Sagaidāmais rezultāts
Ievadi paroli:
abc123
Parole ir pārāk īsa.
'''

parole = input("\nIevadi paroli: ")
a = len(parole)

if a >= 8 and a <= 25:
    print("\nParole ir droša un derīga.\n")
elif a < 8:
    print("\nParole ir pārāk īsa.\n")
elif a > 25:
    print("\nParole ir pārāk gara.\n")