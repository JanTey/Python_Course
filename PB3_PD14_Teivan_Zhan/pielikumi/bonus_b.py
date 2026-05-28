import my_lib.terminal_utils # Modulis termināļa zonas notīrīšanai.
import re

my_lib.terminal_utils.clear_screen() # Termināļa notīrīšana.

teksts = "Mani kontakti: janis@inbox.lv, marite@gmail.com, nepareizs@"

# Šablons
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, teksts)
print(emails, "\n") 
