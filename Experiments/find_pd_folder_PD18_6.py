import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()

"""
Modulis failu skaitīšanai pēc tipa visā projektu struktūrā.
Var saņemt mapes nosaukumu no ārpuses (PD01, PD02, ..., PD18).
"""

import os
import sys

def find_pd_folder(folder_name, start_path='.'):
    """
    Meklē PD mapi pašreizējā mapē un visās augšējās mapēs.
    """
    current = os.path.abspath(start_path)
    
    # Meklē līdz pat saknes mapei
    while True:
        test_path = os.path.join(current, folder_name)
        if os.path.exists(test_path) and os.path.isdir(test_path):
            return test_path
        
        # Ej vienu līmeni augšup
        parent = os.path.dirname(current)
        if parent == current:  # Sasniedzām saknes mapi
            break
        current = parent
    
    return None

def count_files_by_type(directory):
    """
    Saskaita failus pēc to paplašinājuma visā direktorijā UN VISĀS APAKŠDIREKTORIJĀS.
    """
    python_count = 0
    markdown_count = 0
    image_count = 0
    
    if not os.path.exists(directory):
        print(f"KĻŪDA: Mape '{directory}' neeksistē!")
        return {'python': 0, 'markdown': 0, 'images': 0}
    
    print(f"\nPārbauda mapi: {directory}")
    print("Skenē VISAS apakšmapes rekursīvi...")
    print("-" * 50)
    
    for root, dirs, files in os.walk(directory):
        relative_path = os.path.relpath(root, directory)
        if relative_path == '.':
            print(f"\n[Galvenā mape]")
        else:
            print(f"\n[Apakšmape: {relative_path}]")
        
        py_in_folder = 0
        md_in_folder = 0
        img_in_folder = 0
        
        for file in files:
            if file.endswith('.py'):
                python_count += 1
                py_in_folder += 1
                print(f"    📄 Python fails: {file}")
            elif file.endswith('.md'):
                markdown_count += 1
                md_in_folder += 1
                print(f"    📝 Markdown fails: {file}")
            elif file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                image_count += 1
                img_in_folder += 1
                print(f"    🖼️  Attēls: {file}")
        
        if py_in_folder == 0 and md_in_folder == 0 and img_in_folder == 0:
            print("    (nav atrasts neviens .py, .md vai .png/.jpg fails)")
    
    return {
        'python': python_count,
        'markdown': markdown_count,
        'images': image_count
    }


if __name__ == "__main__":
    print()
    
    # Jautā lietotājam
    print("Kādu mapi vēlaties pārbaudīt (ar visām apakšmapēm)?")
    print("Iespējas: PD01, PD02, ..., PD18, vai pilns ceļš")
    print("-" * 40)
    
    user_input = input("Ievadiet mapes nosaukumu: ").strip()
    
    # Pārbauda, vai ievads ir pilns ceļš
    if user_input.startswith('/') or user_input.startswith('.') or ':' in user_input:
        search_path = user_input
    else:
        # Meklē PD mapi
        found_path = find_pd_folder(user_input)
        if found_path:
            search_path = found_path
            print(f"\n✅ Atrasta mape: {search_path}")
        else:
            print(f"\n❌ Mape '{user_input}' nav atrasta pašreizējā vai augšējās mapēs!")
            print(f"   Lūdzu, ievadiet pilnu ceļu uz mapi.")
            search_path = user_input  # saglabā oriģinālu, lai parādītu kļūdu
    
    # Izsauc pārbaudi
    result = count_files_by_type(search_path)
    
    # Izvada kopsavilkumu
    print("\n" + "-" * 50)
    print(f"KOPĀ mapei {user_input}:")
    print(f"  📄 Python faili: {result['python']}")
    print(f"  📝 Markdown faili: {result['markdown']}")
    print(f"  🖼️  Attēlu faili: {result['images']}")
    print()

