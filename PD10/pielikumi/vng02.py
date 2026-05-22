'''
Uzdevums
Izveido funkciju:
signalizet()
Funkcijai jāizvada:
⚠
 Sistēmas brīdinājums!
Izsauc funkciju 3 reizes.
Sagaidāmais rezultāts
⚠️ Sistēmas brīdinājums!
⚠️ Sistēmas brīdinājums!
⚠️Sistēmas brīdinājums!
'''

def signalizet():
    print("⚠️ Sistēmas brīdinājums!")  
       
print()
for i in range(3):  
    signalizet()
print()