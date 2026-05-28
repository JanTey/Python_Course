import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
Dots kods:
import random
laiks = [
"lietus",
"saule",
"vējš"
]
print(random.choise(laiks))
Programma nedarbojas.
Uzdevums:
salabo;
paskaidro:
kādu kļūdu saņēmi;
kā atradi risinājumu.
Sagaidāmais rezultāts
lietus
(vai cita nejauša vērtība)
"""
import random
laiks = [
"lietus",
"saule",
"vējš"
]
print(random.choice(laiks))
# print(random.choise(laiks))
print()