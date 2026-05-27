"""
Programma ar izvēlni, funkciju ievades apstrādei un visu kļūdu apstrādi.
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
    print(f"{'2. Vecuma pārbaude.':<43}<=== Brīdinājums: programma vēl ir izstrādes stadijā!")
    print(f"{'3. Temperatūras pārveidotājs (°C → °F).':<43}<=== Brīdinājums: programma vēl ir izstrādes stadijā!")
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
        
        # JAUTĀJUMS PĒC DARBĪBAS IZPILDĪŠANAS
        print("\n" + "-" * 40)
        turpinat = input("Vai vēlies turpināt darbu ar programmu? (Y/N): ")
        if turpinat.upper() == "N":
            print("Programma beidz darbu. Uz redzēšanos!\n")
            break
        # Ja Y vai Enter - cikls turpinās, izvēlne parādīsies atkārtoti
    
    elif izvele == "2":
        # VECUMA PĀRBAUDE
        print("\n--- VECUMA PĀRBAUDE ---")
        print("Atvainojiet, šis bloks vēl ir izstrādē.")
        print("Lūdzu, izvēlieties citu iespēju - 1.")
        
        # JAUTĀJUMS PĒC NEPAREIZAS IZVĒLES
        print("\n" + "-" * 40)
        turpinat = input("Vai vēlies turpināt darbu ar programmu? (Y/N): ")
        if turpinat.upper() == "N":
            print("Programma beidz darbu. Uz redzēšanos!\n")
            break

    elif izvele == "3":
        # TEMPERATŪRAS PĀRVEIDOTĀJS
        print("\n--- TEMPERATŪRAS PĀRVEIDOTĀJS ---")
        print("Atvainojiet, šis bloks vēl ir izstrādē.")
        print("Lūdzu, izvēlieties citu iespēju - 1.")
        
        # JAUTĀJUMS PĒC NEPAREIZAS IZVĒLES
        print("\n" + "-" * 40)
        turpinat = input("Vai vēlies turpināt darbu ar programmu? (Y/N): ")
        if turpinat.upper() == "N":
            print("Programma beidz darbu. Uz redzēšanos!\n")
            break

    else:
        print("\nNepareiza izvēle! Lūdzu, izvēlies 1, 2, 3 vai N.")
        
        # JAUTĀJUMS PĒC NEPAREIZAS IZVĒLES
        print("\n" + "-" * 40)
        turpinat = input("Vai vēlies turpināt darbu ar programmu? (Y/N): ")
        if turpinat.upper() == "N":
            print("Programma beidz darbu. Uz redzēšanos!\n")
            break