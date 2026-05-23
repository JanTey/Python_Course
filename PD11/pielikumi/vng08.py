'''
Uzdevums
Izveido programmu, kas:
1. sadala komandu vārdos;
2. izvada:
darbību;
mērķi.
Sagaidāmais rezultāts
Darbība:
restartēt
Mērķis:
serveri_01
'''
command = input("\nIevadi termināļa komandu: ") # Ievadi termināļa komandu: restartēt serveri_01
words = command.split()
print("\nDarbība:")
print(words[0])
print("\nMērķis:")
if len(words) > 1:
    print(words[1], "\n")
else:
    print("Nav norādīts mērķis.\n")     