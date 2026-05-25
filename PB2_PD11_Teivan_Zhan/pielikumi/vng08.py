"""
Uzdevums
Izveido:
Pēc tam:
🧩 VNG09 — Artefaktu katalogs
temperatura
statuss
Serveris:
...
BRĪDINĀJUMS
vards
dzivibas
limenis
samazini dzīvības;
palielini līmeni;
izdrukā rezultātu.
"""

games_player = {
    "temperatura": 36.6,
    "statuss": "normāls",
    "vards": "Vilks",
    "dzivibas": 100,
    "limenis": 1,
}

teksts1 = "Spēlētāja statuss spēles sākumā:"
teksts2 = "Spēlētāja statuss spēles beigās:"
print(f"\n{teksts1:<46} {teksts2}\n")
for key, value in games_player.items():
    if key == 'temperatura':
        val2 = round(value + 1.2, 1)
    elif key == 'statuss':
        val2 = 'noguris'
    elif key == 'vards':
        val2 = value
    elif key == 'dzivibas':
        val2 = value - 20
    elif key == 'limenis':
        val2 = value + 1
    else:
        val2 = 0

    print(f"{f'{key}: {value}':<46} {key}: {val2}")
print()
