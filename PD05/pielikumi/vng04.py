'''
Uzdevums
Izveido programmu, kas:
1. palūdz ievadīt nedēļas dienu;
2. pārbauda, vai tā ir sestdiena vai svētdiena;
3. izvada:
“Šodien ir brīvdiena”
vai
“Šodien ir darba diena”.
Sagaidāmais rezultāts
Ievadi dienu:
Svētdiena
Šodien ir brīvdiena.
'''

diena = input("\nIevadi dienu: ").lower()

if diena == "sestdiena" or diena == "svētdiena":
    print("\nŠodien ir brīvdiena.\n")
else:
    print("\nŠodien ir darba diena.\n")
