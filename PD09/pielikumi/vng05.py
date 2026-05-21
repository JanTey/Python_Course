'''
Uzdevums
Lietotāji bieži nejauši ievada liekas atstarpes.
Izveido programmu, kas:
1. saglabā tekstu ar liekām atstarpēm;
2. izvada:
oriģinālo tekstu;
sakopto tekstu.
Sagaidāmais rezultāts
Oriģinālais:
"   sektors_B7   "
Sakoptais:
"sektors_B7"
'''

# Saglabā tekstu ar liekām atstarpēm
teksts = "   sektors_B7   "
print(f"\nOriģinālais: \"{teksts}\"")
print(f"\nSakoptais: \"{teksts.strip()}\"\n")
