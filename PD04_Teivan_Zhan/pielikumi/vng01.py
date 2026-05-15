'''
Uzdevums:
Izveido programmu, kas pajautā lietotāja vecumu un pasaka, vai lietotājs ir pilngadīgs.
Sagaidāmais rezultāts:
Ievadi savu vecumu: 21
Tu esi pilngadīgs.
vai:
Ievadi savu vecumu: 15
Tu vēl neesi pilngadīgs.
'''

vecums = int(input("\nIevadi savu vecumu: "))
if vecums >= 18:
    print(f"\nTu esi pilngadīgs.\n")
else:
    print(f"\nTu vēl neesi pilngadīgs.\n")