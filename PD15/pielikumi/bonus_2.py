import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()

"""
Papildini klasi Gramata.
Pievieno atribūtu:
 izlasita = False
Pievieno metodi:
 atzimet_ka_izlasitu()
Programmai jāspēj parādīt, kuras grāmatas vēl nav izlasītas.
"""
class Gramata:
    def __init__(self, nosaukums, autors, lapas, izlasita):
        self.nosaukums = nosaukums
        self.autors = autors
        self.lapas = lapas
        self.izlasita = izlasita
        
    def atzimet_ka_izlasitu(self):
        if self.izlasita == False:   #if not self.izlasita:
            print(
                f"\nGrāmata: {self.nosaukums}" 
                f"\nautors: {self.autors} \nLapu skaits: {self.lapas}" 
                #f"\nVai esi lasījis grāmatu? {self.izlasita}"
                f"\nVai esi lasījis grāmatu? Nē"
                )      

    def paradit (self):
            izlasita_teksts = "Jā" if self.izlasita else "Nē"
            print(
                f"\nGrāmata: {self.nosaukums}" 
                f"\nautors: {self.autors}" 
                f"\nLapu skaits: {self.lapas}" 
                f"\nVai esi lasījis grāmatu? {izlasita_teksts}"
                )
               
biblioteka = [
    Gramata("Zvejnieka dēls", "Vilis Lācis", 320, True),
    Gramata("Mērnieku laiki", "Reinis un Matīss Kaudzītes", 120, False),
    Gramata("Svešs", "Alberts Camus", 240, True),
    Gramata("Pūt, vējiņi!", "Rainis", 290, False)
]

for gramata in biblioteka:
    # gramata.paradit()
    gramata.atzimet_ka_izlasitu()
print()
