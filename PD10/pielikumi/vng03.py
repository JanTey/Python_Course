'''
Uzdevums
Izveido funkciju:
sasveicinaties(vards)
Funkcijai jāizvada personalizēts sveiciens.
Programmai jāprasa lietotāja vārds ar 
input() .
Sagaidāmais rezultāts
Ievadi vārdu:
Neo
Sveiks, Neo!
'''

def sasveicinaties(vards):
    print()
    print(f"Sveiks, {vards}!")
    print()
    
vards = input("\nIevadi savu vārdu: ")
sasveicinaties(vards)