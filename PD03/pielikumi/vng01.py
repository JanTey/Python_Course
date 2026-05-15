'''Uzdevums:
Izveido programmu, kas:

1.	pajautā lietotāja vārdu,
2.	saglabā to mainīgajā,
3.	sasveicinās ar lietotāju.

Sagaidāmais rezultāts
Kā tevi sauc?
Anna
S̶v̶e̶i̶k̶s̶ Sveika, Anna!
'''

vards = input("Kā tevi sauc? ")
if vards[-1].lower() == "a" or vards[-1].lower() == "e":
    print(f"Sveika, {vards}!")
else:
    print(f"Sveiks, {vards}!")