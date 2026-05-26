"""
Uzdevums
Programma nolasa failu vards.txt un izvada tā saturu ekrānā.
Sagaidāmais rezultāts
Failā saglabāts:
Anna
"""
print("\nFailā saglabāts:\n")

with open("PD12/vards.txt", "r") as f:
    print(f.read() + "\n")
