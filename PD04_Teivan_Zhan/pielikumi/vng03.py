'''
Uzdevums
Izveido vienkāršu piekļuves pārbaudes programmu.
Programma pajautā paroli. Ja parole ir pareiza, programma izvada paziņojumu par piekļuves
atļaušanu. Ja parole nav pareiza, programma izvada atteikumu.
Sagaidāmais rezultāts
Ievadi paroli: python123
Piekļuve atļauta.
'''
parole = input("\nIevadi paroli: ")
if parole == "python123":
    print(f"\nPiekļuve atļauta.\n")
else:
    print(f"\nPiekļuve liegta.\n")