import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()

"""
Izveido klasi Masina.
Katram objektam jābūt:
 markai
 krāsai
 ātrumam
Metodes:
 braukt()
 apstaties()
 paradit_info()
Papildus: izveido 3 mašīnas un saglabā tās sarakstā.
"""
class Masina:
    def __init__(self, marka, krasa, atrums):
        self.marka = marka
        self.krasa = krasa
        self.atrums = atrums
        
    def braukt(self):
        print(f"{self.marka} sāk braukt.")
        
    def apstaties(self):
        print(f"{self.marka} ir apstājusies.")
        
    def paradit_info(self):
        print(f"Mašīna: {self.marka}, Krāsa: {self.krasa}, Ātrums: {self.atrums} km/h")

# Automašīnu saraksts
masinu_saraksts = [
    Masina("Toyota", "Sarkana", 100),
    Masina("BMW", "Melna", 120),
    Masina("Audi", "Sudraba", 110)
]

# Izvadām informāciju par katru mašīnu no saraksta
for m in masinu_saraksts:
    m.paradit_info()
    m.braukt()
    m.apstaties()
    print("-" * 20)