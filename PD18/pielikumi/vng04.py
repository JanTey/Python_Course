import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()

'''
Izveido programmu, kas pārbauda, vai projektā eksistē:
    mape Pielikumi;
    mape atteli;
    fails atskaite_PD18.md.
Programmai jāparāda skaidri paziņojumi.
'''

import os

def check_items(directory, items, item_type='mape'):
    '''Pārbauda, vai norādītajā direktorijā eksistē dotie elementi (mapes vai faili)'''
    
    results = {}
    for item in items:
        path = os.path.join(directory, item)
        if os.path.exists(path):
            if item_type == 'mape':
                print(f'✅ Mape "{item}" atrasta')
            else:
                print(f'✅ Atskaites fails "{item}" atrasts')
        else:
            if item_type == 'mape':
                print(f'❌ Mape "{item}" nav atrasta')
            else:
                print(f'⚠️ Atskaites fails "{item}" nav atrasts')
    return results            
                

if __name__ == "__main__":
    """
    Moduļa testēšana. Šis kods izpildās tikai tad, kad moduli palaiž tieši
    (nevis importē kā moduli).
    """
    my_folders = ['Pielikumi', 'atteli']
    my_files = ['atskaite_PD18.md']
    
    print()
    # Pārbauda mapes
    folder_results = check_items('.', my_folders, 'mape')
    
    # Pārbauda failus
    file_results = check_items('.', my_files, 'fails')
    print()

