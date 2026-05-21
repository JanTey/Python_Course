'''
Uzdevums
Izveido programmu, kas:
1. saņem neapstrādātu ievadi;
2. izmanto:
.strip()
.lower()
.split()
3. izvada:
sakopto tekstu;
sadalīto sarakstu;
pirmo komandas daļu.
Sagaidāmais rezultāts
Sakoptais teksts:
skanēt sektoru_b4
Sadalītais saraksts:
['skanēt', 'sektoru_b4']
Komanda:
skanēt
'''
command = input("\nIevadi termināļa komandu: ") # Ievadi termināļa komandu: skanēt sektoru_b4
command = command.strip().lower()
words = command.split()
print("\nSakoptais teksts:")
print(command)
print("\nSadalītais saraksts:")
print(words)
print("\nKomanda:")
print(words[0], "\n")
