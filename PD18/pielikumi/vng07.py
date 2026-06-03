import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()

"""
Gala programma PD18 — Mapes analizators un projekta kvalitātes pārbaudītājs.
Apvieno struktūras pārbaudi, failu skaitīšanu un nosaukumu pārbaudi.
"""

import os

# Importē funkcijas no esošajiem failiem ar precīziem nosaukumiem
from vng04 import check_items as parbaudit_elementus
from vng05 import check_for_spaces as parbaudit_nosaukumus
from vng06 import count_files_by_type as skaitit_failus


def parbaudit_strukturu(directory='.'):
    """
    Pārbauda projekta struktūru.
    Izmanto funkciju no vng04.py
    
    Parametri
    ---------
    directory : str, optional
        Ceļš uz mapi, kurā veikt pārbaudi (noklusējums - pašreizējā mape)
    
    Atgriež
    -------
    None
        Rezultāti tiek izvadīti konsolē, nevis atgriezti
    """
    my_folders = ['Pielikumi', 'atteli']
    my_files = ['atskaite_PD18.md']
    
    # Pārbauda mapes un failus
    parbaudit_elementus(directory, my_folders, 'mape')
    parbaudit_elementus(directory, my_files, 'fails')


def find_pd_folder(folder_name, start_path='.'):
    """
    Meklē PD mapi pašreizējā mapē un visās augšējās mapēs.
    
    Parametri
    ---------
    folder_name : str
        Mapes nosaukums (piemēram, 'PD18')
    start_path : str, optional
        Kur sākt meklēšanu (noklusējums - pašreizējā mape)
    
    Atgriež
    -------
    str or None
        Pilnu ceļu uz mapi, ja atrasta, vai None, ja nav atrasta
    """
    current = os.path.abspath(start_path)
    
    while True:
        test_path = os.path.join(current, folder_name)
        if os.path.exists(test_path) and os.path.isdir(test_path):
            return test_path
        
        parent = os.path.dirname(current)
        if parent == current:  # Sasniedzām saknes mapi
            break
        current = parent
    
    return None


if __name__ == "__main__":
    """
    Galvenā programmas daļa.
    Izpildās tikai tad, kad skriptu palaiž tieši (nevis importē kā moduli).
    """
    print()
    print("=" * 50)
    print("PROJEKTA PĀRBAUDES ATSKAITE")
    print("=" * 50)
    
    print("\nKādu mapi vēlaties pārbaudīt?")
    print("Iespējas: PD01, PD02, ..., PD18, vai pilns ceļš")
    print("-" * 40)
    
    user_input = input("Ievadiet mapes nosaukumu: ").strip()
    
    # Nosaka, kuru mapi pārbaudīt
    if user_input.startswith('/') or user_input.startswith('.') or ':' in user_input or user_input.startswith('~'):
        search_path = os.path.expanduser(user_input)
        display_name = search_path
    else:
        found_path = find_pd_folder(user_input)
        if found_path:
            search_path = found_path
            display_name = user_input
        else:
            search_path = user_input
            display_name = user_input
    
    # Pārbauda, vai mape eksistē
    if not os.path.exists(search_path):
        print(f"\n❌ KĻŪDA: Mape '{display_name}' nav atrasta!")
        print(f"   Meklēts: {search_path}")
    else:
        print(f"\nSkatās mapē: {display_name}")
        print("──────────────────────────────────────────────")
        
        # Izsauc trīs galvenās funkcijas (izvads notiek to iekšpusē)
        parbaudit_strukturu(search_path)
        skaitit_failus(search_path)
        parbaudit_nosaukumus(search_path)
        
        # Izvada pabeigšanas statusu
        print()
        print("Struktūras pārbaude pabeigta.")
        print("Failu skaitīšana pabeigta.")
        print("Nosaukumu pārbaude pabeigta.")
        
        print("\n" + "=" * 50)
        print("Pārbaude pabeigta.")
        print("=" * 50)
    
    print()