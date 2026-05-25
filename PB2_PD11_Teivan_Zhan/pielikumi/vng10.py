"""
Uzdevums
Programma:
1. prasa ievadīt vārdu;
2. prasa vecumu;
3. izveido vārdnīcu;
4. pievieno pilsētu;
5. izvada:
Objekts izveidots:
{ ... }
"""

vards = input("\nIevadi vārdu: ")
vecums = int(input("Ievadi vecumu: "))
pilseta = input("Ievadi pilsētu: ")

persona = {
    'vards': vards,
    'vecums': vecums,
    'pilseta': pilseta
}

print(f"\nObjekts izveidots: {persona}\n")
for key, value in persona.items():
    print(f"  {key.capitalize()}: {value}")
print()

