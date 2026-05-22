'''
Uzdevums
Palaid abas programmas un novēro rezultātus.
Variants A
def tests():
print("Neo")
rezultats = tests()
print(rezultats)
Variants B
def tests():
return "Neo"
rezultats = tests()
print(rezultats)
Jautājumi
1. Kāpēc pirmajā variantā parādās 
2. Kurš variants atgriež vērtību?
3. Kāpēc 
return ir svarīgs?
'''

def tests1():
    # Выводим сразу строку, без деления на аргументы
    print("\nNeo")

rezultats = tests1()
print(rezultats)

print('=================================')

def tests2():
    return "Neo"

rezultats = tests2()
print(rezultats, "\n")
