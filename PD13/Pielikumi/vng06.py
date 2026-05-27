import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
skaitli = [10,20,30]
summa = 0
for skaitlis in skaitli:
summa = summa + 1
print(summa)
Pievieno print().
Atrodi kļūdu.
Sagaidāmais rezultāts
60
"""

skaitli = [10,20,30]
summa = 0
for skaitlis in skaitli:
#    summa = summa + 1
    summa = summa + skaitlis
print(f"\n{summa}\n")