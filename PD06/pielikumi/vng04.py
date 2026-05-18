'''
Uzdevums
Programma atkārtoti prasa ievadīt paroli.
Kamēr parole nav:
python123
programma turpina prasīt ievadi.
Kad parole ir pareiza, programma izvada:
Piekļuve atļauta!
Sagaidāmais rezultāts
Ievadi paroli: abc
Ievadi paroli: 123
Ievadi paroli: python123
Piekļuve atļauta!
'''

while True:
    password = input("Ievadi paroli: ")
    if password == "python123":
        print("Piekļuve atļauta!")
        break

