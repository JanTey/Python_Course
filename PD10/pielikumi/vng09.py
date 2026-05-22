'''
Uzdevums
Izveido funkcijas:
parbaudit_degvielu()
parbaudit_temperaturu()
parbaudit_signalus()
Galvenajai programmai:
1. jāizsauc visas funkcijas;
2. jāizvada pilns diagnostikas ziņojums.
Sagaidāmais rezultāts--- DIAGNOSTIKA --
✅
 Degvielas sistēma stabila
⚠
 Temperatūra paaugstināta
✅
 Signāli stabili
'''

def parbaudit_degvielu():
    return "✅ Degvielas sistēma stabila"
def parbaudit_temperaturu():
    return "⚠️ Temperatūra paaugstināta"
def parbaudit_signalus():
    return "✅ Signāli stabili"

print("\n--- DIAGNOSTIKA ---")
print(parbaudit_degvielu())
print(parbaudit_temperaturu())
print(parbaudit_signalus())
print()