"""
Uzdevums
Programma prasa ievadīt vārdu un saglabā to failā vards.txt.
Sagaidāmais rezultāts
Ievadi vārdu:
Anna
Vārds saglabāts.
Failā:
Anna
"""

vards = input("\nIevadi vārdu: \n")

with open("PD12/vards.txt", "w") as f:
    f.write(vards)

print("\nVārds saglabāts.\n")

with open("PD12/vards.txt", "r") as f:
    print(f"Failā:\n{f.read()}\n")