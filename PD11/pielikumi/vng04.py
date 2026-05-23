'''
Uzdevums
Izveido programmu, kas:
1. saglabā lietotāja ievadītu kodu;
2. izvada:
tekstu ar mazajiem burtiem;
tekstu ar LIELAJIEM burtiem.
Sagaidāmais rezultāts
Oriģinālais teksts:
Neo-Admin
Mazie burti:
neo-admin
Lielie burti:
NEO-ADMIN
'''
# 1. saglabā lietotāja ievadītu kodu;
teksts = input("\nIevadi tekstu: ")   
print("\nOriģinālais teksts:\n" + teksts)
print("\nMazie burti:\n" + teksts.lower())
print("\nLielie burti:\n" + teksts.upper() + "\n")