'''
Uzdevums
Programma avarē.
Noskaidro:
 - kāpēc,
 - un salabo to.
    vecums = input("Cik tev ir gadi? ")
    print(vecums + 1)
Sagaidāmais rezultāts
Cik tev ir gadi?
20
21    
'''
vecums = input("\nCik tev ir gadi? ")

print('''\nFunkcija input() vienmēr atgriež tekstu (string). 
Lai ievadītos datus izmantotu aritmētiskajās operācijās, 
tie ir jāpārvērš skaitļos, izmantojot int() vai float(), 
pretējā gadījumā radīsies kļūda.''')

print(f"\n{vecums} \n{int(vecums) + 1}\n")