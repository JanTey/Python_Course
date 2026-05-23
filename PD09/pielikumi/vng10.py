'''
Uzdevums
Programma satur vairākas kļūdas.
Atrodi un izlabo tās.
teksts = "   NEO-77"
teksts.strip
teksts.lower()
print(teksts)
Jautājumi pārdomām
Kāpēc 
.strip nedarbojās?
Kāpēc teksts nepārvērtās mazajos burtos?
Kāpēc rezultāts neizmainījās?
'''

teksts = "   NEO-77"
# teksts.strip
# teksts.lower()

teksts = teksts.strip()
teksts = teksts.lower()

print("\n", teksts, "\n", sep="")
