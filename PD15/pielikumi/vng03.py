import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
Izveido klasi Kruze.
Sākumā krūze ir tukša.
Klasei jābūt:
atribūtam piepildita
metodei ieliet()
metodei izdzert()
metodei paradit_stavokli()
Programmai jāparāda, kā krūzes stāvoklis mainās.
Sagaidāmais rezultāts
Krūze ir tukša.
Krūze piepildīta!
Krūze ir pilna.
Tēja izdzerta.
Krūze ir tukša.
"""
class Kruze:
    def __init__(self):
        # Inicializē krūzi kā tukšu (False)
        self.piepildita = False
        
    def ieliet(self):
        # Pārbauda, vai krūze jau nav pilna
        if self.piepildita: 
            print("Nevar ieliet – krūze jau ir pilna!")
        else:               
            # Ja krūze ir tukša, piepilda to
            self.piepildita = True
            print("Krūze piepildīta!") 
            
    def izliet(self):
        # Pārbauda, vai krūze ir pilna
        if self.piepildita:  
            self.piepildita = False
            print("Krūze ir izlieta!")
        else:                
            # Ja krūze jau ir tukša, izliet neko nevar
            print("Nevar izliet – krūze jau ir tukša!") 
        
    def paradit_stavokli(self):
        # Izvada informāciju par krūzes pašreizējo stāvokli
        if self.piepildita:
            print("Krūze ir pilna.\n") 
        else:
            print("Krūze ir tukša.\n")    
            
# Izveido jaunu objekta instanci
mana_kruze = Kruze()

# Demonstrē metodes darbībā
mana_kruze.paradit_stavokli()

mana_kruze.izliet()
mana_kruze.paradit_stavokli()

mana_kruze.ieliet()
mana_kruze.paradit_stavokli()

mana_kruze.ieliet()
mana_kruze.paradit_stavokli()

mana_kruze.izliet()
mana_kruze.paradit_stavokli()