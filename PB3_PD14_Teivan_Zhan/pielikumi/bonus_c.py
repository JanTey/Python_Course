import my_lib.terminal_utils # Modulis termināļa zonas notīrīšanai.


my_lib.terminal_utils.clear_screen() # Termināļa notīrīšana.

# 1. Sveiciena funkcija
vards = "Janis"
from mans_riku_komplekts import sveiciens # Importē funkcijas no moduļa
sveiciens(vards)

# 2. Kapināšanas funkcija
from mans_riku_komplekts import kapina # Importē funkcijas no moduļa
kapina(3, 4)

# 3. Teksta formatēšanas funkcija
from mans_riku_komplekts import formatet_teikumu # Importē funkcijas no moduļa
nevīžīgs_teksts = "  šIS  ir  SLIKTI   uzrakstīTS   teikums   "
skaists_teksts = formatet_teikumu(nevīžīgs_teksts)
print(skaists_teksts, "\n")