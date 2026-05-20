'''
Uzdevums
Izveido sarakstu 
vini ar vismaz 4 vīnu nosaukumiem.
Izdrukā:
pirmo vīnu;
otro vīnu;
trešo vīnu.
Sagaidāmais rezultāts
Pirmais vīns: Merlot
Otrais vīns: Rioja
Trešais vīns: Chianti
'''

vins_names = "Merlot, Rioja, Chianti, Charlie, Domenico, Sangiovese, Barolo, Brunello, Amarone, Valpolicella"
number_names = "pirmais, otrais, trešais, ceturtais, piektais, sestais, septītais, astotais, devītais, desmitais"

vini = vins_names.split(', ')
skaitlis = number_names.split(', ')

print()
for i in range(len(vini)):
    if i < 3:
        print(f"{skaitlis[i].title()} vīns: {vini[i]}")
print()