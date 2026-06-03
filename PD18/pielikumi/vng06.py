import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()

"""
Modulis failu skaitīšanai pēc tipa visā projektu struktūrā.
Var saņemt mapes nosaukumu no ārpuses (PD01, PD02, ..., PD18).
"""

import os

def count_files_by_type(directory):
    """Saskaita failus pēc to paplašinājuma visā direktorijā un visās apakšdirektorijās."""
    
    python_count = 0
    markdown_count = 0
    image_count = 0
    
    # Pārbauda, vai mape eksistē
    if not os.path.exists(directory):
        return None
    
    # os.walk() apstaigā visu direktoriju un visas apakšdirektorijas
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_count += 1
            elif file.endswith('.md'):
                markdown_count += 1
            elif file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                image_count += 1
    
    return {
        'python': python_count,
        'markdown': markdown_count,
        'images': image_count
    }


def find_pd_folder(folder_name, start_path='.'):
    """
    Meklē PD mapi pašreizējā mapē un visās augšējās mapēs.
    """
    current = os.path.abspath(start_path)
    
    while True:
        test_path = os.path.join(current, folder_name)
        if os.path.exists(test_path) and os.path.isdir(test_path):
            return test_path
        
        parent = os.path.dirname(current)
        if parent == current:
            break
        current = parent
    
    return None


if __name__ == "__main__":
    print()
    
    # Prasa lietotājam ievadīt mapes nosaukumu
    print("Kādu mapi vēlaties pārbaudīt (ar visām apakšmapēm)?")
    print("Iespējas: PD01, PD02, ..., PD18, vai pilns ceļš")
    print("-" * 40)
    
    user_input = input("Ievadiet mapes nosaukumu: ").strip()
    
    # Nosaka, kuru mapi pārbaudīt
    if user_input.startswith('/') or user_input.startswith('.') or ':' in user_input or user_input.startswith('~'):
        # Pilns ceļš
        search_path = os.path.expanduser(user_input)
        display_name = search_path
    else:
        # Meklē PD mapi
        found_path = find_pd_folder(user_input)
        if found_path:
            search_path = found_path
            display_name = user_input  # Parāda tikai nosaukumu, nevis pilnu ceļu
        else:
            search_path = user_input
            display_name = user_input
    
    # Pārbauda, vai mape eksistē
    if not os.path.exists(search_path):
        print(f"\n❌ KĻŪDA: Mape '{display_name}' nav atrasta!")
        print(f"   Meklēts: {search_path}")
    else:
        # Skaita failus
        result = count_files_by_type(search_path)
        
        # Izvada rezultātu vienkāršā formātā
        print()
        print(f"Skatās mapē: {display_name}")
        print("──────────────────────────────────────────────")
        print(f"Python faili: {result['python']}")
        print(f"Markdown faili: {result['markdown']}")
        print(f"Attēlu faili: {result['images']}")
    
    print()
