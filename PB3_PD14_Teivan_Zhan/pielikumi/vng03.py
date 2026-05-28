import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
Izveido failu:
vng03_aprekini.py
Izveido funkcijas:
dubultot()
triskarsot()
Failā:
vng03.py
importē moduli;
izvada šodienas datumu;
izsauc abas funkcijas.
Sagaidāmais rezultāts
Datums:
2026-05-26
10
15
"""
from datetime import date
import vng03_aprekini as calc

today = date.today()
print(f"Datums:")
print(f"{today}\n")

skaitlis = 5
print(calc.dubultot(skaitlis))
print(calc.triskarsot(skaitlis))
print()