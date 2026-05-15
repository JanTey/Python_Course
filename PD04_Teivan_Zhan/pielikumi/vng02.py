'''
Uzdevums
Izveido programmu, kas pajautā temperatūru un dod vienkāršu ieteikumu.
Ja temperatūra ir lielāka par 38, programma izvada brīdinājumu par drudzi. Citādi
programma pasaka, ka temperatūra nav paaugstināta.
Sagaidāmais rezultāts
Ievadi temperatūru: 39
Temperatūra ir paaugstināta. Ieteicams atpūsties.
'''

temperatura = float(input("\nIevadi temperatūru: "))
if temperatura >= 37:
    print(f"\nTemperatūra ir paaugstināta. Ieteicams atpūsties.\n")
else:
    print(f"\nTemperatūra nav paaugstināta.\n")