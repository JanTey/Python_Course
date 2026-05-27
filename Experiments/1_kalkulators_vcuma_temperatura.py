import my_lib.terminal_utils

my_lib.terminal_utils.clear_screen()
"""
Programma ar izvēlni, funkciju ievades apstrādei un visu kļūdu apstrādi.
Программа с меню выбора, функцией обработки ввода и обработкой всех ошибок.
"""

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


def izvelne():
    print("\n" + "=" * 40)
    print("   IZVĒLNIEKS")
    print("=" * 40)
    print("1. Kalkulators (dalīšana)")
    print("2. Vecuma pārbaude")
    print("3. Temperatūras pārveidotājs (°C → °F)")
    print("=" * 40)
    print("N - iziet no programmas")
    print("=" * 40)


# Galvenā programma
while True:
    izvelne()
    izvele = input("Izvēlies darbību (1/2/3/N): ")
    
    if izvele.upper() == "N":
        print("Programma beidz darbu. Uz redzēšanos!\n")
        break
    
    if izvele == "1":
        # KALKULATORS ar visu kļūdu apstrādi
        print("\n--- KALKULATORS (dalīšana) ---")
        print("(Lai izietu uz galveno izvēlni, ievadi N)")
        
        while True:
            # Ievada pirmo skaitli
            skaitlis1, iziet = ievade_ar_parbaudi("Ievadi pirmo skaitli: ", "")
            if iziet:
                break
            
            # Ievada otro skaitli
            skaitlis2, iziet = ievade_ar_parbaudi("Ievadi otro skaitli: ", "")
            if iziet:
                break
            
            # Mēģina veikt dalīšanu
            try:
                n1 = float(skaitlis1)
                n2 = float(skaitlis2)
                rezultats = n1 / n2
                print(f"{n1} / {n2} = {rezultats:.2f}")
                break  # Veiksmīga dalīšana - iziet no cikla
            except ZeroDivisionError:
                print("Kļūda: Nevar dalīt ar nulli! Mēģini vēlreiz.")
                # Turpina ciklu - prasa ievadīt vēlreiz
            except Exception as e:
                # Apstrādā jebkuru citu neparedzētu kļūdu
                print(f"Neparedzēta kļūda: {e}")
                break
    
    elif izvele == "2":
        # VECUMA PĀRBAUDE
        print("\n--- VECUMA PĀRBAUDE ---")
        print("(Lai izietu uz galveno izvēlni, ievadi N)")
        
        while True:
            vecums, iziet = ievade_ar_parbaudi("Ievadi savu vecumu: ", "int")
            if iziet:
                break
            
            # Pārbauda vecumu
            try:
                if vecums >= 18:
                    print("Tu esi pilngadīgs!")
                else:
                    print(f"Tev vēl jāgaida {18 - vecums} gadi.")
                break
            except Exception as e:
                print(f"Neparedzēta kļūda: {e}")
                break
    
    elif izvele == "3":
        # TEMPERATŪRAS PĀRVEIDOTĀJS
        print("\n--- TEMPERATŪRAS PĀRVEIDOTĀJS ---")
        print("(Lai izietu uz galveno izvēlni, ievadi N)")
        
        while True:
            celsijs, iziet = ievade_ar_parbaudi("Ievadi temperatūru °C: ", "float")
            if iziet:
                break
            
            # Pārveido temperatūru
            try:
                farenheits = celsijs * 9/5 + 32
                print(f"{celsijs}°C = {farenheits:.1f}°F")
                break
            except Exception as e:
                print(f"Neparedzēta kļūda: {e}")
                break
    
    else:
        print("\nNepareiza izvēle! Lūdzu, izvēlies 1, 2, 3 vai N.")