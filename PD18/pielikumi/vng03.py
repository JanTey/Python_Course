import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()

'''Izveido programmu, kas pārskata pašreizējās mapes saturu un pie 
katra elementa parāda, vai tas ir fails vai mape.'''

import os

def check_directory_contents():
    current_directory = os.getcwd()
    
    with os.scandir(current_directory) as entries:
        for entry in entries:
            if entry.is_file():
                print(f"{entry.name} -- Fails")
            elif entry.is_dir():
                print(f"{entry.name} -- Mape")

if __name__ == "__main__":
    print()
    check_directory_contents()
    print()