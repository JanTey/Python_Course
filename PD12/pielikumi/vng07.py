"""
Uzdevums
Izveido programmu, kas failā rindas.txt ieraksta trīs rindas:
Pirmā rinda
Otrā rinda
Trešā rinda
Izmanto \n.
Sagaidāmais rezultāts
Failā:
Pirmā rinda
Otrā rinda

Trešā rinda
"""


with open("PD12/rindas.txt", "w", encoding="utf-8") as fails:
    fails.write("Pirmā rinda\n")
    fails.write("Otrā rinda\n")
    fails.write("\nTrešā rinda\n")

with open("PD12/rindas.txt", "r", encoding="utf-8") as fails:
    print("\n" + fails.read())
