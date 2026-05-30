import my_lib.terminal_utils # Modulis termināļa zonas notīrīšanai.
my_lib.terminal_utils.clear_screen() # Termināļa notīrīšana.

import os

# Nosakām mapi, kurā atrodas šis skripts
PAŠREIZĒJĀ_MAPE = os.path.dirname(os.path.abspath(__file__))
# Norādām pilnu ceļu failam, kurā saglabāsim datus
FAILA_NOSAUKUMS = os.path.join(PAŠREIZĒJĀ_MAPE, "dzivnieki.txt")

# Klase Dzivnieks - veidne dzīvnieka objektu izveidei
class Dzivnieks:
    # Konstruktors - izsaucas automātiski, veidojot jaunu objektu
    def __init__(self, suga, vards, vecums):
        self.suga = suga      # Dzīvnieka suga (piem., "suns", "kaķis")
        self.vards = vards    # Dzīvnieka vārds
        self.vecums = vecums  # Dzīvnieka vecums
        
    # Metode, kas izvada dzīvnieka informāciju ekrānā
    def paradit(self):
        print(f"Suga: {self.suga}")
        print(f"Vards: {self.vards}")
        print(f"Vecums: {self.vecums}\n")
    
    # Pārvērš objektu par teksta rindiņu saglabāšanai failā
    def to_string(self):
        return f"{self.suga}|{self.vards}|{self.vecums}"
    
    # Statiskā metode - izveido objektu no teksta rindiņas (pretējs to_string())
    @staticmethod
    def from_string(line):
        suga, vards, vecums = line.strip().split('|')
        return Dzivnieks(suga, vards, vecums)


# Saglabā visu dzīvnieku sarakstu teksta failā
def saglabat_faila(dzivnieki, fails_nosaukums=FAILA_NOSAUKUMS):
    with open(fails_nosaukums, 'w', encoding='utf-8') as fails:
        for dzivnieks in dzivnieki:
            fails.write(dzivnieks.to_string() + '\n')
    print(f"\nDati saglabāti failā '{fails_nosaukums}'.")


# Ielādē dzīvnieku sarakstu no teksta faila (ja fails eksistē)
def ieladet_no_faila(fails_nosaukums=FAILA_NOSAUKUMS):
    dzivnieki = []
    if os.path.exists(fails_nosaukums):
        with open(fails_nosaukums, 'r', encoding='utf-8') as fails:
            for line in fails:
                if line.strip():
                    dzivnieki.append(Dzivnieks.from_string(line))
        print(f"Ielādēti {len(dzivnieki)} dzīvnieki no faila '{fails_nosaukums}'.")
    else:
        print(f"Fails '{fails_nosaukums}' neeksistē. Tiks izveidots jauns saraksts.")
    return dzivnieki


# ========== GALVENĀ PROGRAMMA ==========
print("=" * 40)
print("DZĪVNIEKU REĢISTRĀCIJA")
print("=" * 40)
print(f"Dati tiks saglabāti failā: {FAILA_NOSAUKUMS}")

# Mēģinām ielādēt iepriekš saglabātos dzīvniekus (ja fails eksistē)
dzivnieku_saraksts = ieladet_no_faila()

# Cilks, kurā lietotājs var pievienot jaunus dzīvniekus
while True:
    print("\n--- Jauna dzīvnieka ievade ---")
    pievienot = input("Vai pievienot vēl vienu dzīvnieku? (y/n): ")
    if pievienot.lower() == "n":
        break  # Iziet no cikla, ja lietotājs ievada 'n'
    
    # Prasām lietotājam ievadīt dzīvnieka datus
    suga = input("Ievadiet dzīvnieka sugu: ")
    vards = input("Ievadi vārdu: ")
    vecums = input("Ievadi vecumu: ")
    
    # Izveidojam jaunu Dzivnieks objektu un pievienojam sarakstam
    dzivnieku_saraksts.append(Dzivnieks(suga, vards, vecums))

# Saglabājam visu sarakstu failā (pārraksta veco saturu)
saglabat_faila(dzivnieku_saraksts)

# Izvadām visus dzīvniekus ekrānā
print("\n--- Visi dzīvnieki ---")
for dzivnieks in dzivnieku_saraksts:
    dzivnieks.paradit()