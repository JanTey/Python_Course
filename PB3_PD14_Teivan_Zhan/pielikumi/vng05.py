import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
Izvēlies vienu moduli:
math
random
datetime
Izmanto:
help(...)
dir(...)
Atrodi:
vienu funkciju;
paskaidro ko tā dara;
uzraksti piemēru.
Sagaidāmais rezultāts
Piemērs:
 Izvēlētais modulis:
 math
 Funkcija:
 factorial()
 Piemērs:
 factorial(5)=120
"""

import datetime

print("Izvēlētais modulis:")
print("datetime")
print("\nFunkcija:")
print("datetime.now()")
print("\nPaskaidrojums:")
print("Funkcija now() atgriež pašreizējo datumu un laiku.")
print("\nPiemērs:")
print(f"datetime.now() = {datetime.datetime.now()}")

print("\n--- dir(datetime) ---")
print(dir(datetime))

print("\n--- help(datetime.datetime.now) ---")
print("now(tz=None) class method of datetime.datetime")
print("    Returns new datetime object representing current time local to tz.")
print("    If no tz is specified, uses local timezone.\n")
