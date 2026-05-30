import my_lib.terminal_utils # Modulis termināļa zonas notīrīšanai.
my_lib.terminal_utils.clear_screen() # Termināļa notīrīšana.

"""
Izveido programmu, kur lietotājs pats ievada vairākus dzīvniekus.
Programma jautā:
 Vai pievienot vēl vienu dzīvnieku? jā/nē
Visi dzīvnieki tiek saglabāti sarakstā.
Beigās programma izvada visu dzīvnieku sarakstu.
"""
class Dzivnieks:
    def __init__(self, suga, vards, vecums):
        self.suga = suga
        self.vards = vards
        self.vecums = vecums
        
    def paradit(self):
        print(f"Suga: {self.suga}")
        print(f"Vards: {self.vards}")
        print(f"Vecums: {self.vecums}\n")    

dzivnieku_saraksts = []

while True:
    print("\n--- Jauna dzivnika ievade ---")
    pievienot = input("Vai pievienot vēl vienu dzīvnieku? y/n: ")
    if pievienot.lower() == "n":
        break
    suga = input("Ievadiet dzīvnieka sugu: ")
    vards = input("Ievadi vardu: ")
    vecums = input("Ievadi vecumu: ")
    
    dzivnieku_saraksts.append(Dzivnieks(suga, vards, vecums))

print("\n--- Visi dzivnieki ---")
for dzivnieks in dzivnieku_saraksts:
    dzivnieks.paradit()