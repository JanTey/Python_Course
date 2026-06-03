import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()

'''Izveido programmu, kas:
1. nolasa pašreizējās mapes saturu;
2. ar ciklu izvada visus atrastos elementus;
3. katru failu vai mapi parāda jaunā rindā.'''

import os

satura_saraks = os.listdir()
print("Pašreizējās mapes saturs:\n")
for elements in satura_saraks:
    print(elements)
print()