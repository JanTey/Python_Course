'''
Uzdevums
Izveido programmu, kas:
1. saglabā termināļa komandu;
2. sadala to vārdos;
3. izvada iegūto sarakstu.
Sagaidāmais rezultāts
['restartēt', 'serveri_01']
'''

print()
command = input("\nIevadi termināļa komandu: ") # command = "restartēt serveri_01"
words = command.split()
print("\n", words, "\n")