import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()

''' noskaidro pašreizējo darba karti un izvada to uz ekrāna '''
import os

print("\nPašreizējā darba karte:", os.getcwd())
print()