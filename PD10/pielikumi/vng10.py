'''
Uzdevums
Izdomā un izveido savu funkciju.
Piemēri:
piekļuves validācija.
Funkcijai jāizmanto:
parametrs;
return ;
vismaz viens 
if .
'''

import subprocess
import sys
def pārbaudīt_sistēmu(parole):
    # 1. Pārbaude uz latīņu šriftu (ASCII)
    if not parole.isascii():
        print("\n❌ Kļūda: Atļauti tikai latīņu burti!")
        return False # Пароль не подошел
        
    # 2. Paroles pārbaude
    if parole == "asd":
        ludzu()
        return True # Сигнал успеха! Пароль верный.
    else:
        if i == 4:
            print("\n❌ Maksimālais mēģinājumu skaits sasniegts. Sistēma bloķēta.")
        else:
            print("\n⚠️ Parole netika pieņemta! Mēģiniet vēlreiz.")
            return False # Parole nedarbojās

def ludzu():
    print("\n✅ Parole pieņemta. Degvielas sistēma: NOMINĀLA.")

# Galvenā programma
for i in range(1, 5):
    ievade = input(f"\nMēģinājums {i}/4. Ievadi parole: ")
    
    # Izsauciet funkciju cikla iekšpusē un pārbaudiet tās atbildi
    uzvara = pārbaudīt_sistēmu(ievade)
    
    if uzvara == True:
        print("\nSistēma aktivizēta. Palaižam nākamo programmu...")
        import os
            
        # 2. Atrodiet precīzu mapi, kurā fiziski atrodas pašreizējais vng10.py fails.
        tekoša_mape = os.path.dirname(__file__)
            
        # 3. Savienojiet ceļu ar mapi ar vēlamā faila nosaukumu vng09.py
        cela_uz_failu = os.path.join(tekoša_mape, "vng06.py")
            
        #4. Palaidiet, izmantojot precīzu pilnu ceļu
        subprocess.run([sys.executable, cela_uz_failu])
        exit()