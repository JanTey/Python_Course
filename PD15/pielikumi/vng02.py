import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
Izveido klasi Gramata.
Katrai grāmatai jābūt:
nosaukumam
autoram
lapu skaitam
Izveido metodi paradit_info(), kas izvada grāmatas informāciju.
Izveido vismaz divas grāmatas.
Sagaidāmais rezultāts
Grāmata: Zvejnieka dēls
Autors: Vilis Lācis
Lapu skaits: 320
"""

class Gramata:
    def __init__(self, nosaukums, autors, lapas):
        self.nosaukums = nosaukums
        self.autors = autors
        self.lapas = lapas
    def paradit (self):
        print(f"\nGrāmata: {self.nosaukums} \nautors: {self.autors} \nLapu skaits: {self.lapas}")

biblioteka = [
    Gramata("Zvejnieka dēls", "Vilis Lācis", 320),
    Gramata("Mērnieku laiki", "Reinis un Matīss Kaudzītes", 120),
    Gramata("Svešs", "Alberts Camus", 240),
    Gramata("Pūt, vējiņi!", "Rainis", 290)
]

for gramata in biblioteka:
    gramata.paradit()
print()
