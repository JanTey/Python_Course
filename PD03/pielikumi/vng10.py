'''
Uzdevums
Izveido savu mazo interaktīvo programmu.
Dienas budžeta kalkulators

Sagaidāmais rezultāts
1. čeks. Ievadiet čeka summu: 23.3
Vai vēlaties pievienot jaunu čeku? (Y/N): y
2. čeks. Ievadiet čeka summu: 50
Vai vēlaties pievienot jaunu čeku? (Y/N): y
3. čeks. Ievadiet čeka summu: 5.47
Vai vēlaties pievienot jaunu čeku? (Y/N): n

Jūsu dienas tēriņu summa ir: 78.77 EUR
'''

kopa = 0  # Mainīgais kopējai summai
turpinat = "Y"  # Mainīgais Cikla turpināšanas kontrolei
ceka_numurs = 1  # Mainīgais čeku skaitim

print("\nDienas budžeta kalkulators\n")
while turpinat.upper() == "Y":
    
    # Pieprasām pašreizējā čeka summu
    summa = float(input(f"{ceka_numurs}. čeks. Ievadiet čeka summu: "))
    kopa += summa  # Pieskaitām kopējai summai
    
    # Jautājam, vai lietotājs vēlas pievienot vēl vienu kvīti
    turpinat = input("Vai vēlaties pievienot jaunu čeku? (Y/N): ")
    ceka_numurs += 1

# Galīgā rezultāta aprēķināšana un izvadīšana
print(f"\nJūsu dienas tēriņu summa ir: {kopa:.2f} EUR\n")