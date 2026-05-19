'''
Uzdevums
Izveido programmu, kas atkārtoti prasa ievadīt paroli.
Pareizā parole: python123
Ja parole ir nepareiza, programma turpina jautāt.
Kad parole ievadīta pareizi:
Piekļuve atļauta
Sagaidāmais rezultāts
Ievadi paroli:
abc
Ievadi paroli:
123
Ievadi paroli:
python123
Piekļuve atļauta
'''

print()
parole = ""
while parole != "python123":
    parole = input("Ievadi paroli: ")
print("Piekļuve atļauta")
print()    