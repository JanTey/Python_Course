'''
Uzdevums
Izveido sarakstu 
inventars ar 3 cyberpunk stila priekšmetiem.
Pajautā lietotājam vēl vienu priekšmetu ar 
Pievieno to sarakstam ar 
.append() .
Izdrukā atjaunoto inventāru.
Sagaidāmais rezultāts
input() .
Ievadi jaunu inventāra priekšmetu: NanoBlade
['Optical Camouflage', 'Neural Chip', 'Drone', 'NanoBlade']
'''

inventari = ['Optical Camouflage', 'Neural Chip', 'Drone']
new_inventars = input("\nIevadi jaunu inventāra priekšmetu: ")
inventari.append(new_inventars)
print()
print(inventari)
print()
