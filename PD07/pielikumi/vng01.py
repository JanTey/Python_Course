'''
Uzdevums
Izveido programmu, kas 5 reizes izvada tekstu:
Python ir interesants!
Sagaidāmais rezultāts
Python ir interesants!
Python ir interesants!
Python ir interesants!
Python ir interesants!
Python ir interesants!
'''

print("\nIzmantojam *for* ciklu:\n")
for i in range(5):
    print("Python ir interesants!")   
print()

print("\nIzmantojam *while* ciklu:\n")
i = 0
while i < 5:
    print("Python ir interesants!")
    i += 1 
print()
