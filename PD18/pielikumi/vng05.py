import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()

"""
Modulis failu nosaukumu pārbaudei visā projektu struktūrā.
Pārbauda visus failus galvenajā mapē un visās apakšmapēs.
"""

import os

def check_for_spaces(directory):
    
    """Pārbauda, vai failu nosaukumos ir atstarpes VISĀS apakšmapēs."""
    
    files_with_spaces = []
    
    # os.walk() apstaigā visu direktoriju un visas apakšdirektorijas
    for root, dirs, files in os.walk(directory):
        for file in files:
            if ' ' in file:
                full_path = os.path.join(root, file)
                files_with_spaces.append(full_path)
                print(f'BRĪDINĀJUMS: Faila nosaukumā atrasta atstarpe:\n {full_path}')
    
    if not files_with_spaces:
        print('Failu nosaukumos atstarpes nav atrastas.')
    
    return files_with_spaces


if __name__ == "__main__":
    """
    Moduļa testēšana. Šis kods izpildās tikai tad, kad moduli palaiž tieši
    (nevis importē kā moduli).
    """
    print()
    print("Pārbauda visus failus mapē un apakšmapēs...")
    print("-" * 50)
    
    result = check_for_spaces('.')
    
    print("-" * 50)
    if result:
        print(f"Atrasti {len(result)} faili ar atstarpēm nosaukumos:")
        for path in result:
            print(f"  - {path}")
    print()
