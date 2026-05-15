'''
Uzdevums (## Задание)
Izveido programmu, kas:

1.	pajautā lietotāja vecumu,
2.	pārvērš ievadi par skaitli,
3.	aprēķina vecumu nākamgad,
4.	izvada rezultātu.
Sagaidāmais rezultāts
Cik tev ir gadi?
20
Nākamgad tev būs 21 gadi.
'''

vecums = input("Cik ir tev gadi? ")
vecums = int(vecums)
vecums_nakamgad = vecums + 1
print(f"Nākamgad tev būs {vecums_nakamgad} gadi.")