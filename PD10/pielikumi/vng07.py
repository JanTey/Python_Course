'''
Uzdevums
Dots kods:
vards1 = input("1. vārds: ")
vards1 = vards1.strip()
vards1 = vards1.lower()
vards2 = input("2. vārds: ")
vards2 = vards2.strip()
vards2 = vards2.lower()
print(vards1)
print(vards2)
Pārveido šo programmu, izmantojot funkciju:
sakopt_vardu()
'''

def sakopt_vardu(vards):
    vards = vards.strip()
    vards = vards.lower()
    return vards

vards1 = input("\n1. vārds: ")
vards1 = sakopt_vardu(vards1)

vards2 = input("\n2. vārds: ")
vards2 = sakopt_vardu(vards2)
print()
print(vards1)
print(vards2, "\n" )   
