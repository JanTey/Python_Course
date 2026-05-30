import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()

"""
Uzdevums
Izveido klasi Suns.
Katram sunim jābūt vārdam.
Klasei jābūt metodei rej(), kas izvada tekstu:
 Riko saka: Vau!
Izveido vismaz divus dažādus suņus un liec abiem riet.
Sagaidāmais rezultāts
Riko saka: Vau!
Bella saka: Vau!
"""
class Suns:
    def __init__(self, vards):
        self.vards = vards
    def rej (self):
        print(self.vards, "saka: Vau!")

suni = ["Rico", "Bella"]

for vards in suni:
    Suns(vards).rej()
print()
# suns1 = Suns("Riko")
# suns2 = Suns("Bella")
# suns1.rej()
# suns2.rej()