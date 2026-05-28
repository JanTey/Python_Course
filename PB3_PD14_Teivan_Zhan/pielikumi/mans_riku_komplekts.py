import re

def sveiciens(name):
    print(f"\nSveiks, {name}!\n")

def kapina(skaitlis, pakape):
    """Funkcija paaugstina skaitli dotajā pakāpē"""
    rezultats = skaitlis ** pakape
    print(f"{skaitlis} ^ {pakape} = {rezultats}\n")
    return rezultats

def formatet_teikumu(teksts):
    """
    Funkcija formatē tekstu kā pareizu teikumu:
    - likvidē liekos (dubultos un vairāk) atstarpes
    - sākumu ar lielo burtu
    - beigās pieliek punktu, ja tā nav
    """
    # 1. Likvidē liekās atstarpes (vairākus atstarpju simbolus aizstāj ar vienu)
    teksts = re.sub(r'\s+', ' ', teksts)
    
    # 2. Noņem atstarpes sākumā un beigās
    teksts = teksts.strip()
    
    # 3. Pārveido pirmo burtu par lielo, pārējos par mazajiem
    if len(teksts) > 0:
        teksts = teksts[0].upper() + teksts[1:].lower()
    
    # 4. Pārliecinās, ka beigās ir punkts
    if not teksts.endswith('.'):
        teksts += '.'
    
    return teksts