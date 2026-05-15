'''
Uzdevums
Programma nedarbojas.
Atrodi kļūdu un salabo programmu.

    vards = input("Vārds: ") 
    print(f"Sveiks, {vards}!")    =====> {vards}  
    
Sagaidāmais rezultāts
Vārds:
Anna
Sveika, Anna!
'''

vards = input("\nVards: ")
if vards[-1].lower() == "a" or vards[-1].lower() == "e":
    print(f"Sveika, {vards}!\n")
else:
    print(f"\nSveiks, {vards}!\n")