'''
Uzdevums
Izpēti programmu:
lietus = False
if not lietus:
    print("Var doties pastaigā")
else:
    print("Labāk palikt mājās")
Pēc tam:
1. nomaini False uz True ;
2. palaid programmu vēlreiz;
3. apraksti atšķirību atskaitē.
Sagaidāmais rezultāts 
Var doties pastaigā vai Labāk palikt mājās
'''

print("\nPirmais tests:")
lietus = False
if not lietus:
    print(f"\nJa lietus = {lietus}: Var doties pastaigā\n")
else:
    print(f"\nJa lietus = {lietus}: Labāk palikt mājās\n")    
    
print("\nOtrais tests:")
lietus = True
if not lietus:
    print(f"\nJa lietus = {lietus}: Var doties pastaigā\n")
else:
    print(f"\nJa lietus = {lietus}: Labāk palikt mājās\n")    