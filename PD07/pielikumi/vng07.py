'''
Uzdevums
Izveido vienkāršu izvēlni:
1 - Sasveicināties
2 - Parādīt dienas novēlējumu
0 - Iziet
Programmai jādarbojas ciklā, līdz lietotājs izvēlas 0 .
Sagaidāmais rezultāts
1 - Sasveicināties
2 - Parādīt dienas novēlējumu
0 - Iziet
Izvēle: 1
Sveiki!
Izvēle: 2
Lai tev laba diena!
Izvēle: 0
Programma beigusies
'''

print()
print("1 - Sasveicināties")
print("2 - Parādīt dienas novēlējumu")
print("0 - Iziet")
x = ""

while x != 0 :
    x = int(input("\nIzvēle: "))
    if x == 1 :
        print("Sveiki!")
    elif x == 2:
        print("Lai tev laba diena!")   
print("\nProgramma beigusies\n")
