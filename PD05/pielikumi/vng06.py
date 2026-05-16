'''
Uzdevums
Programma satur kļūdas.
Salabo tās.
vecums = int(input("Ievadi vecumu: "))
if vecums = 18:        ============> === BOJĀTS KODS ===> if vecums == 18:
    print("Tev ir 18 gadi")
Sagaidāmais rezultāts
Ievadi vecumu:
18
Tev ir 18 gadi
'''

vecums = int(input("\nIevadi vecumu: "))
if vecums == 18:
    print(f"\nVecums ir {vecums}.\n")
else:
    print("\nVecums nav 18.\n")