"""
Uzdevums
Izveido īsu programmu.
Nosacījumi:
līdz ~20 rindām;
lietotāja ievade;
viena iespējama kļūda;
try/except.
Piemēri:
kalkulators;
vecuma pārbaude;
temperatūras pārveidotājs.
"""

#ienkāršs kalkulators (dalīšana) ar kļūdu apstrādi.
#Lietotājs var turpināt rēķināt vai iziet programmu.

def ievade_ar_parbaudi(prompt, tips, izejas_atslega="N"):
    while True:
        ievade = input(prompt)
        
        # Pārbauda, vai lietotājs vēlas iziet
        if ievade.upper() == izejas_atslega:
            return None, True
        
        # Mēģina pārveidot ievadi
        try:
            if tips == "int":
                vertiba = int(ievade)
            elif tips == "float":
                vertiba = float(ievade)
            else:
                vertiba = ievade
            return vertiba, False
        except ValueError:
            print(f"Kļūda: Lūdzu, ievadi {tips} tipa vērtību!")
            # Turpina ciklu - prasa vēlreiz


# Galvenā programma
print("\n" + "=" * 50)
print("   KALKULATORS (dalīšana)")
print("=" * 50)
print("Lai izietu no programmas, ievadi N jebkurā brīdī.")
print("=" * 50)

while True:
    print("\n" + "-" * 40)
    
    # Ievada pirmo skaitli
    skaitlis1, iziet = ievade_ar_parbaudi("Ievadi pirmo skaitli: ", "float")
    if iziet:
        print("\nProgramma beidz darbu. Uz redzēšanos!")
        break
    
    # Ievada otro skaitli
    skaitlis2, iziet = ievade_ar_parbaudi("Ievadi otro skaitli: ", "float")
    if iziet:
        print("\nProgramma beidz darbu. Uz redzēšanos!\n")
        break
    
    # Mēģina veikt dalīšanu
    try:
        rezultats = skaitlis1 / skaitlis2
        print(f"\n{skaitlis1} / {skaitlis2} = {rezultats:.2f}")
    except ZeroDivisionError:
        print("\nKļūda: Nevar dalīt ar nulli! Mēģini vēlreiz.")
        continue  # Sāk ciklu no sākuma
    except Exception as e:
        print(f"\nNeparedzēta kļūda: {e}")
        break
    
    # Jautājums pēc veiksmīga aprēķina
    print("\n" + "-" * 40)
    turpinat = input("Vai vēlies turpināt rēķināt? (Y/N): ")
    if turpinat.upper() == "N":
        print("\nProgramma beidz darbu. Uz redzēšanos!")
        break
    # Ja Y vai Enter - cikls turpinās