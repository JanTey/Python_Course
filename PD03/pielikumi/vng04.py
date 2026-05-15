'''
Uzdevums
Izveido programmu, kas pajautā:
vārdu, mīļāko krāsu, mīļāko ēdienu.
Programmai jāizvada īss personalizēts teksts.
Sagaidāmais rezultāts
Kā tevi sauc? / Anna
Kāda ir tava mīļākā krāsa? / zila
Kāds ir tavs mīļākais ēdiens? / pica
Annai patīk zila krāsa un pica.
'''
vards = input("Kā tevi sauc? ")
krausa = input("Kāda ir tava mīļākā krāsa? ")
edieni = input("Kāds ir tavs mīļākais ēdiens? ")

# Vārdnīca: nominatīvs -> datīvs
datīvs_vārdnīca = {
    "Anna": "Annai",
    "Jānis": "Jānim",
    "Ilze": "Ilzei",
    "Toms": "Tomam",
    "Marta": "Martai",
    "Pēteris": "Pēterim",
    "Artis": "Artim",
    "Dārta": "Dārtai"
}

if vards in datīvs_vārdnīca:
    print(f"{datīvs_vārdnīca[vards]} patīk {krausa} krāsa un {edieni}.")
else:
    print(f"Sveiki, {vards}! Tava mīļākā krāsa ir {krausa}, un tavs mīļākais ēdiens ir {edieni}.")
