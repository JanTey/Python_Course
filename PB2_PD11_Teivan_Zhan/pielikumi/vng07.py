"""
Uzdevums
Izveido:
serveris = {
}
Lauki:
nosaukums
ip
temperatura
statuss
Programma izvada:
Serveris:
...
Ja temperatūra >70:
BRĪDINĀJUMS
"""

serveris = {
    "nosaukums": "Serveris01",
    "ip": "192.168.1.1",
    "temperatura": 70,
    "statuss": "aktīvs"
}
serveris["temperatura"] = int(input("\nIevadi temperatūru: "))
print("\nServeris:\n")
for key, value in serveris.items():
    print(f"  {key}: {value}")
print()
if serveris["temperatura"] > 70:
    print("\nBBRĪDINĀJUMS: temperatūra ir pārāk augsta!\n")
else:
    print("Temperatūra ir normas robežās.\n")    