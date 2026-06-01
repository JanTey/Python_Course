import my_lib.terminal_utils # Modulis termināļa zonas notīrīšanai.
my_lib.terminal_utils.clear_screen() # Termināļa notīrīšana.

class Dzivnieks:
    def __init__(self, suga, vards, vecums):
        self.suga = suga
        self.vards = vards
        self.vecums = vecums
        
    def iegut_info(self):
        return f"Suga: {self.suga}\nVards: {self.vards}\nVecums: {self.vecums}\n"    
        
    def paradit(self):
        print(f"Suga: {self.suga}")
        print(f"Vards: {self.vards}")
        print(f"Vecums: {self.vecums}\n")

    def formatet_ierakstam(self):
        return f"{self.suga}|{self.vards}|{self.vecums}\n"        

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

print("\n--- Visi jaunie dzīvnieki ---")
with open("Experiments/dzivnieki_base/dzivnieki.txt", "a", encoding="utf-8") as files:
    for dzivnieks in dzivnieku_saraksts:
        dzivnieks.paradit()          
        files.write(dzivnieks.formatet_ierakstam())
    
print("\n--- Saturs no faila ---")
with open("Experiments/dzivnieki_base/dzivnieki.txt", "r", encoding="utf-8") as files:
    saturs = files.read()
    print(saturs)