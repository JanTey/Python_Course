"""
Uzdevums
Programma:
1. prasa ievadīt īsu piezīmi;
2. saglabā to failā piezime.txt;
3. nolasa šo failu;
4. izvada saturu ekrānā.
Sagaidāmais rezultāts
Ievadi piezīmi:
Šodien mācos failus.
Saglabātā piezīme:
Šodien mācos failus.
"""

piezime = input("\nIevadi piezīmi: \n")

with open("PD12/piezime.txt", "w") as f:
    f.write(piezime)

# print(f"\nSaglabātā piezīme:")

with open("PD12/piezime.txt", "r") as f:
    print("\nSaglabātā piezīme:\n" + f.read() + "\n")
