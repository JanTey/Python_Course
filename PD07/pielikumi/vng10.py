'''
Uzdevums
Izveido programmu, kas:
ļauj ievadīt 3 vārdus;
saglabā tos sarakstā;
beigās izvada visus vārdus.
💡
 Šis ir neliels ieskats nākamajā tēmā.
Sagaidāmais rezultāts
Ievadi vārdu:
Anna
Ievadi vārdu:
Jānis
Ievadi vārdu:
Pēteris
Ievadītie vārdi:
Anna
Jānis
Pēteris
'''

vardu_saraksts = []     # Izveidosim tukšu sarakstu, kurā tiks saglabāti ievadītie vārdiim vārdus
print()                 # Lai atvieglotu lasīšanu, ekrānā tiek parādīta tukša rinda

for i in range(3):
    vardu_saraksts.append(input("Ievadi vārdu: ")) 

print("\nIevadītie vārdi: \n")
for vards in vardu_saraksts:      # Lai izvadītu visus vārdus, izmantojam for ciklu, kas iterē cauri sarakstam
    print(vards)
print()