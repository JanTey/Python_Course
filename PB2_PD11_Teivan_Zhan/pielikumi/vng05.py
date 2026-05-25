"""
Uzdevums
Dots kods:
persona = {
"vards":"Neo"
}
print(persona["telefons"])
Izlabo.
Programmai jāizvada:
Telefons nav norādīts
"""

persona = {
"vards":"Neo"
}
print(persona.get("telefons", "\nTelefons nav norādīts\n"))