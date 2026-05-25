"""
Uzdevums
Izveido artefaktu.
Obligāti:
nosaukums
retums
vertiba
Papildini ar vismaz 2 laukiem.
"""

def print_artifact(data):
    print("\nArtefakta dati:")
    for key, value in data.items():
        print(f"  {key.capitalize()}: {value}")
    print()    

artefakts = {
    'nosaukums': 'Zelta Krūze',
    'retums': 'Ļoti reta',
    'vertiba': 1000,
}

print_artifact(artefakts)

artefakts.update({
    'izgatavots': 'Seno laiku meistars',
    'materiāls': 'Zelts',
    'statuss': 'Eksponāts muzejā'
})
print_artifact(artefakts)