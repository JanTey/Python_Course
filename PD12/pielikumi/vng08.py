"""
Uzdevums
Dots kods:
with open("nav_tada_faila.txt", "r", encoding="utf-8") as fails:
    saturs = fails.read()
print(saturs)
Programma izraisa kļūdu.
Izlabo situāciju vienā no diviem veidiem:
1. vispirms izveido failu;
2. vai nomaini faila nosaukumu uz tādu, kas eksistē.
Sagaidāmais rezultāts
Programma nolasa failu bez kļūdas.
"""

# with open("nav_tada_faila.txt", "r", encoding="utf-8") as fails:  
# Files "nav_tada_faila.txt" not found ==> error
with open("PD12/dienasgramata.txt", "r", encoding="utf-8") as fails:
    saturs = fails.read()
    
print(saturs)