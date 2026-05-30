import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
Izveido klasi Dzivnieks.
Katram dzīvniekam jābūt:
 vārdam
 sugai
 skaņai
Izveido metodi sasveicinaties(), kas izvada, piemēram:
 Es esmu suns Riko. Es saku: Vau!
Izveido vismaz 3 dzīvniekus.
Saglabā tos sarakstā.
Ar ciklu izsauc katra dzīvnieka metodi sasveicinaties().
Sagaidāmais rezultāts
 Es esmu suns Riko. Es saku: Vau!
 Es esmu kaķis Muris. Es saku: Mjau!
 Es esmu papagailis Koko. Es saku: Čiv!
"""
class Dzivnieks:
    def __init__(self, vards, suga, skana):
        self.vards = vards
        self.suga = suga
        self.skana = skana
    def sasveicinaties (self):
        print(f"\nEs esmu {self.suga} {self.vards}. Es saku: {self.skana}")

dzivnieku_saraksts = [
    Dzivnieks("Riko", "suns", "Vau!"),
    Dzivnieks("Muris", "kaķis", "Mjau!"),
    Dzivnieks("Koko", "papagailis", "Čiv!"),
]

for dzivnieks in dzivnieku_saraksts:
    dzivnieks.sasveicinaties()
print()