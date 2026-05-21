'''
Uzdevums
Izveido programmu, kas pārbauda:
vai drošības žurnālā eksistē vārds:
BRĪDINĀJUMS
Izmanto:
.lower()
in
Sagaidāmais rezultāts
Vai sistēmā ir brīdinājums?
True
'''

security_log = "2024-06-01 12:00:00 - BRĪDINĀJUMS: Neautorizēta piekļuve mēģinājums"
print(f"\nVai sistēmā ir brīdinājums?\n{ 'brīdinājums' in security_log.lower() }\n")
