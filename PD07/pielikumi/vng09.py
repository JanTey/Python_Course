'''
Uzdevums
Izveido programmu, kas:
prasa ievadīt 5 skaitļus;
aprēķina to summu;
beigās izvada rezultātu.
Sagaidāmais rezultāts
Ievadi skaitli: 5
Ievadi skaitli: 3
Ievadi skaitli: 7
Ievadi skaitli: 2
Ievadi skaitli: 1
Summa = 18
'''

akumulator = 0 # mainīgais, kurā tiks uzkrāta summa
print()
for i in range(1, 6):
   # katru reizi, kad tiek ievadīts skaitlis, tas tiek pieskaitīts akumulatoram
   akumulator = akumulator + int(input("Ievadi skaitli: "))  
print(f"\nSumma = {akumulator}\n")