import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
Programmai jāizvada:
kvadrātsakne no 144;
nejaušs laikapstākļu scenārijs.
Piemēram:
Kvadrātsakne:
12.0
Prognoze:
migla
Izmanto:
math
random
"""

import math
import random

a = random.randint(1, 200)
print(f"Kvadrātsakne: \n{math.sqrt(a)}\n")
