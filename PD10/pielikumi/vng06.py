'''
Uzdevums
Izveido funkciju:
parbaudit_degvielu(litri)
Ja degvielas daudzums ir mazāks par 20:
⚠
 KRITISKS: Zems degvielas līmenis!
Pretējā gadījumā:
✅
 Degvielas sistēma: NOMINĀLA.
Sagaidāmais rezultāts
⚠
 KRITISKS: Zems degvielas līmenis!
'''

def parbaudit_degvielu(litri):
    if litri < 20:
        return "⚠️ KRITISKS: Zems degvielas līmenis!"
    else:
        return "✅ Degvielas sistēma: NOMINĀLA."

ievade = int(input("\nCik daudz degvielas ir jūsu automašīnā?: "))

pazinojums = parbaudit_degvielu(ievade)

print("\n", pazinojums, "\n")
