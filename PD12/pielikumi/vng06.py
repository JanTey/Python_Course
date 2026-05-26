"""
Uzdevums
Izveido programmu, kas failā dienasgramata.txt pieraksta klāt vienu rindu:
Šodien es iemācījos saglabāt datus.
Izmanto režīmu "a".
Sagaidāmais rezultāts
Ja programmu palaiž vairākas reizes, failā parādās vairākas rindas.
Šodien es iemācījos saglabāt datus.
Šodien es iemācījos saglabāt datus.
Šodien es iemācījos saglabāt datus.
"""

for i in range(3):
    with open("PD12/dienasgramata.txt", "a", encoding="utf-8") as fails:
        fails.write("Šodien es iemācījos saglabāt datus.\n")
    
with open("PD12/dienasgramata.txt", "r", encoding="utf-8") as fails:
    print("\n" + fails.read())