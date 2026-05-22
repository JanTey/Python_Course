'''
Uzdevums
Izveido funkciju:
sakopt_signalu(teksts)
Funkcijai:
1. jānotīra liekās atstarpes;
2. jāpārveido teksts uz mazajiem burtiem;
3. jāatgriež rezultāts ar 
return .
Sagaidāmais rezultāts
neo
'''

def sakopt_signalu(teksts):
    print()
    teksts = teksts.strip()  
    teksts = teksts.lower() 
    print()
    return teksts

# teksts = input("\nIevadi tekstu: ")
# rezultats = sakopt_signalu(teksts)
rezultats = sakopt_signalu(input("\nIevadi tekstu: "))
print(rezultats, "\n")
