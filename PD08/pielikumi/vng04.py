'''
Uzdevums
Izveido sarakstu 
misijas ar vismaz 4 kosmosa misijām.
Izmantojot 
for ciklu, izdrukā katru misiju atsevišķā rindā.
Sagaidāmais rezultāts
Apollo 11
Voyager 1
Cassini
Artemis
'''

text = "Sputnik 1 (PSRS, 1957); Apollo 11 (ASV, 1969); Voyager 1 (ASV, 1977); "\
                  "Voyager 2 (ASV, 1977); Hubble Space Telescope (ASV/ESO, 1990); " \
                  "Cassini–Huygens (ASV/ESO/Itālija, 1997); International Space Station (ISS) " \
                  "(vairākas valstis, 1998–pašlaik); Mars Curiosity Rover (ASV, 2011); " \
                  "James Webb Space Telescope (ASV/ESO/Kanāda, 2021); Artemis I (ASV, 2022)"

print()

kosmosa_misijas = text.split("; ")
for i in kosmosa_misijas:
    print(i)

print()