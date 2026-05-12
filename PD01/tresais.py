# Definējam mainīgo vecums ar vērtību 25
vecums = 25

# 1. veids: Izmantojot f-virkni (modernākā un vienkāršākā metode) (Способ 1: Использование f-строки
# (самый современный и простой способ))

print(f"Jūsu vecums ir {vecums} gadi. -- Izmantojot f-virkni")


""" 
    2. veids: Eksplicīta tipa pārveidošana, izmantojot str() (Способ 2: Явное преобразование типа через str())
    Tas ir tieši tas, kas domāts ar "pārveidojiet to par teksta virkni" (Это именно то, что подразумевается 
    под "преобразуйте в текстовую строку")
"""

vecums_teksts = str(vecums)
print("Jūsu vecums ir " + vecums_teksts + " gadi. -- izmantojot str()")
