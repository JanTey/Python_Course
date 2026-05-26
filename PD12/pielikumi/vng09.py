"""
Uzdevums
Programma:
1. prasa ievadīt vārdu;
2. saglabā to failā viesi.txt;
3. izmanto režīmu "a";
4. pēc tam nolasa visu failu;
5. izvada visus viesus.
Sagaidāmais rezultāts
Ievadi vārdu:
Anna

Visi viesi:

Juris
Anna
"""
vards = input("\nIevadi vārdu: \n")
with open("PD12/viesi.txt", "a", encoding="utf-8") as fails:
    fails.write(vards + "\n")

with open("PD12/viesi.txt", "r", encoding="utf-8") as fails:
    print("\nVisi viesi:\n\n" + fails.read())
