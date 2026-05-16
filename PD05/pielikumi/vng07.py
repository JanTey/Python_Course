'''
Uzdevums
Izveido programmu, kas:
1. palūdz ievadīt: vecumu; vai cilvēkam ir skolēna apliecība (jā /nē);
2. piešķir atlaidi, ja: vecums ir mazāks vai vienāds ar 18 vai ir skolēna apliecība.
3. izvada: “Atlaide piešķirta” vai “Atlaide netika piešķirta”.
Sagaidāmais rezultāts
Ievadi vecumu:
20
Vai tev ir skolēna apliecība?
jā
Atlaide piešķirta.
'''

vecums = int(input("\nIevadi vecumu: "))
apleciba = input("Vai tev ir apliecība? (jā/nē): ")
if (vecums >= 7 and vecums <= 18) or (vecums > 18 and apleciba == "jā"):
    print(f"\nAtlaide piešķirta.\n")
elif vecums < 7:
    print("\nAaaaaaaaa...\n")
else:
    print("\nAtlaide netika piešķirta.\n")