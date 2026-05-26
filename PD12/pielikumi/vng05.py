"""
Uzdevums
Izveido programmu:
with open("tests.txt", "w", encoding="utf-8") as fails:
    fails.write("Pirmā rinda\n")
with open("tests.txt", "w", encoding="utf-8") as fails:
    fails.write("Otrā rinda\n")
with open("tests.txt", "r", encoding="utf-8") as fails:
    saturs = fails.read()
print(saturs)

Palaid programmu un atbildē pieraksti:
kura rinda palika failā?
kāpēc pirmā rinda pazuda?
Sagaidāmais rezultāts
Otrā rinda
"""
with open("PD12/tests.txt", "w", encoding="utf-8") as fails:
    fails.write("Pirmā rinda\n")
    
with open("PD12/tests.txt", "w", encoding="utf-8") as fails:
    fails.write("Otrā rinda\n")
    
with open("PD12/tests.txt", "r", encoding="utf-8") as fails:
    saturs = fails.read()
    
print("\n" + saturs)

