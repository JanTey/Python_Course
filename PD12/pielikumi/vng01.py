"""
Uzdevums
Izveido programmu, kas failā pirmais_fails.txt ieraksta tekstu:
Mana programma sāk atcerēties.
Izmanto:
with open(...)
Sagaidāmais rezultāts
Mapē parādās fails:
pirmais_fails.txt
Tajā ir teksts:
Mana programma sāk atcerēties.
"""

with open("PD12/pirmais_fails.txt", "w") as f:
    f.write("Mana programma sāk atcerēties.")