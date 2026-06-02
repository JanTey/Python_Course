# Praktiskā darba atskaite

---

# 1. Vispārīgā informācija

* Vārds, Uzvārds:** Zhan Teivan 
* Grupa:**  Daugavpils_77978_11.05.2026.-05.06.2026
* Praktiskā darba kods: PD17
* Datums:** 2026-06-01  

[Mana praktiskā darba mape GitHub platformā](https://github.com/JanTey/Python_Course/blob/main/PD17/atskaite_PD17.md)

---

# 2. Darba mērķis

Šajā darbā bija paredzēts apgūt:

- Saprotamu mainīgo nosaukumu izvēli (snake_case)
- Noderīgu komentāru rakstīšanu (kāpēc, nevis ko)
- Koda sadalīšanu funkcijās (modularitāte)
- Funkciju dokumentēšanu ar docstring
- Projekta dokumentācijas veidošanu (README.md)

Tika attīstītas šādas uzturēšanas prasmes:

- **Analīzes prasme** - atpazīt problēmas kodā (neskaidri nosaukumi, lieki komentāri)
- **Koda refaktorēšanas prasme** - uzlabot kodu bez funkcionalitātes maiņas
- **Dokumentēšanas prasme** - rakstīt saprotamu docstring un README
- **Kļūdu labošanas prasme** - identificēt un novērst loģikas kļūdas
- **Tehniskā parāda samazināšanas prasme** - uzlabot koda kvalitāti
- **Projektu strukturēšanas prasme** - organizēt failus un mapes

---

# 3. Darba konteksts

Hidrojot PD17 uzdevumu, es analizēju vienkāršu lineāru skriptu, kas aprēķināja atradumu svaru kopējo un vidējo vērtību. Šis bija pasniedzēja sagatavotais sākotnējais kods, kas demonstrēja tipiskas iesācēju kļūdas. Mana uzdevums bija pārveidot šo skriptu par labi strukturētu projektu, izmantojot saprotamus mainīgo nosaukumus, funkcijas, komentārus un dokumentāciju.

---

# 4. Sākotnējais stāvoklis

Pirms darba uzsākšanas sistēma atradās šādā stāvoklī:

- **Dokumentācija nebija pieejama** - kodā nebija docstring, trūka README.md faila
- **Bija zināmas problēmas** - neskaidri mainīgo nosaukumi (x, y, z), bezjēdzīgs skaitītājs, lieki komentāri
- **Bija tehniskais parāds** - kods nebija sadalīts funkcijās, trūka datu validācijas un kļūdu apstrādes
- **Nebija izmaiņu pieprasījumu** - uzdevums tika dots kā mācību projekts
- **Nebija nepieciešama migrācija** - darbs notika vienā vidē

Sākotnējais kods bija lineārs skripts, kas darbojās, bet bija grūti lasāms, uzturams un paplašināms.

---

# 5. Darba izpilde

## 5.1 Uzdevums 1

Pārveidot kodu [`vng01_slikti_nosaukumi.py`](./pielikumi/vng01_slikti_nosaukumi.py) tā, 
lai mainīgo nosaukumi būtu saprotami (izmanto snake_kase).
Rezultātu saglabāt failā vng01_laboti_nosaukumi.py
[`vng01_laboti_nosaukumi.py`](./pielikumi/vng01_laboti_nosaukumi.py)

### Ko darīju
Analizēju sākotnējo kodu atbilstībai PEP 8 formātam (snake_case stils).

### Kā veicu darbu
Tika mainīti mainīgo nosaukumi un pārveidoti funkcijas print() argumenti, lai saprastu to 
vērtības, kā arī pievienoti komentāri, lai saprastu, ko šī programma dara.

### Rezultāts

```python id="p62h2r"

# Programmas "Arheoloģisko izrakumu analizators" darbības rezultātu parādīšanas piemērs

atradumu_skaits = 5
kopējais_svars = 427
vecākais_vecums = 1200

print("\nARHEOLOĢISKO IZRAKUMU ANALIZĀCIJAS REZULTĀTI\n")
print("Atradumu skaits: ", atradumu_skaits)
print("Kopējais svars: ", kopējais_svars)
print("Vecākais vecums: ", vecākais_vecums)
print()
```
---

## 5.2 Uzdevums 2

Nepieciešams analizēt sākotnējo programmu pēc loģikas un atbilstības 
PEP 8 komentāru rakstīšanas noteikumiem, kā arī izlabot kodu:

```python id="p62h2r"  
atradumu_skaits = 0

atradumu_skaits = atradumu_skaits + 1  # Pieskaita viens
print(atradumu_skaits)  # Izvada atradumu skaitu

if atradumu_skaits > 0:
    print("Ir atradumi")  # Izvada tekstu
    print("Nav atradumu")
```

### Ko darīju

Es analizēju sākotnējā koda loģiku un atklāju, ka skaitītājam šajā programmā 
nav jēgas, jo vērtība tiek noteikta jau sākotnēji. Tāpat es analizēju komentārus 
pēc nepieciešamības un liekuma kritērijiem, saskaņā ar PEP 8 noteikumiem.

### Kā veicu darbu

1. Noņēmu skaitītāju - atradumu_skaits = atradumu_skaits + 1 , jo stingri 
   noteiktā mainīgā vērtība padara skaitītāja palielināšanu bezjēdzīgu.

2. Izlaboju izvades loģiku - pievienoju else zaru gadījumam, kad atradumu 
   nav (mainīgā vērtība ir 0).

3. Izdzēsu liekos komentārus - noņēmu komentārus, kas izskaidroja acīmredzamu 
   sintaksi.

4. Pievienoju vienīgo nepieciešamo komentāru - noformēju to kā docstring ar 
   trīskārtīgām pēdiņām, kas izskaidro programmas mērķi, nevis tās acīmredzamo 
   sintaksi un loģiku.

### Rezultāts

[`vng02_komentari.py`](./pielikumi/vng02_komentari.py)

```python id="p62h2r"    
"""Programmas loģika, lai paziņotu arheologam, vai attiecīgajā vietā
ir atradumi un cik to ir.
"""

atradumu_skaits = 2

# atradumu_skaits = atradumu_skaits + 1
#print(atradumu_skaits)

if atradumu_skaits > 0:
    print("Ir atradumi")
    print(atradumu_skaits)
else:    
    print("Nav atradumu")
```
---

## 5.3 Uzdevums 3

Sākotnējā programma ir dota:

```python id="p62h2r"   
dati = [15, 120, 30, 250, 12]

kopejais_svars = sum(dati)
videjais_svars = kopejais_svars / len(dati)

print("Kopējais svars:", kopejais_svars)
print("Vidējais svars:", videjais_svars)
```
Pārveido kodu tā, lai tajā būtu vismaz trīs funkcijas:
```python id="p62h2r" 
def nolasit_datus():
...
def analizet_datus(dati):
...
def paradit_rezultatu(rezultati):
...
```
### Ko darīju

Es analizēju sākotnējo kodu, kas bija vienkāršs lineārs skripts. Tajā 
nebija funkciju, nebija klases, un kods izpildījās secīgi no augšas uz 
leju. Es sapratu, ka šādu kodu nevar atkārtoti izmantot, to ir grūti 
testēt, un tas neatbilst modulārās programmēšanas principiem.

Es arī pamanīju, ka sākotnējā kodā trūkst kļūdu apstrādes (piemēram, 
dalīšanas ar nulli, ja datu saraksts ir tukšs), trūkst dokumentācijas, 
un tas nav sadalīts 
loģiskos blokos.

### Kā veicu darbu

1. Izveidoju klasi SvaruAnalizators - lai apvienotu visas saistītās 
   darbības vienuviet.
2. Pievienoju trīs metodes (funkcijas) klases iekšpusē:
   * kopejais_svars() - aprēķina atradumu kopējo svaru
   * videjais_svars() - aprēķina atradumu vidējo svaru
   * izvadit() - izvada rezultātus uz ekrāna
3. Pievienoju dokumentāciju (docstring) - klasei un katrai metodei, lai 
   izskaidrotu to mērķi.
4. Pievienoju konstruktoru __init__ - lai nodotu datus klasē, veidojot 
   objektu.
5. Pievienoju bloku if __name__ == "__main__" - lai kodu varētu izmantot
   kā moduli vai palaist tieši.

### Rezultāts

[`vng03_funkcijas.py`](./pielikumi/vng03_funkcijas.py)

```python id="p62h2r" 

"""Programma atradumu svaru analīzei - aprēķina kopējo un vidējo svaru."""

class SvaruAnalizators:
    """Analizē atradumu svarus un veic nepieciešamos aprēķinus."""
    
    def __init__(self, dati):
        self.dati = dati
    
    def kopejais_svars(self):
        """Aprēķina un atgriež kopējo svaru."""
        return sum(self.dati)
    
    def videjais_svars(self):
        """Aprēķina un atgriež vidējo svaru."""
        return sum(self.dati) / len(self.dati)
    
    def izvadit(self):  # ← Теперь внутри класса (с отступом)
        """Izvada aprēķinu rezultātus konsolē."""
        print("Kopējais svars:", self.kopejais_svars())
        print("Vidējais svars:", self.videjais_svars())

# Programmas palaišana
if __name__ == "__main__":
    dati = [15, 120, 30, 250, 12]
    analizators = SvaruAnalizators(dati)
    analizators.izvadit()
```
---

## 5.2 Uzdevums 4

Ir jāanalizē iepriekšējā uzdevuma programma, lai nodrošinātu atbilstību 
PEP 8 dokumentācijas rakstīšanas noteikumiem - docstring.

Oriģinālā programma:

[`vng03_funkcijas.py`](./pielikumi/vng03_funkcijas.py)

### Ko darīju

Es analizēju pirmkodu un pamanīju, ka pirmkodā ir nepilnīga dokumentācija, 
kas ir pretrunā ar PEP 8 (docstrng) prasībām, kā arī trūkst kļūdu apstrādes — 
dalīšanas ar nulli, ja datu saraksts ir tukšs.

### Kā veicu darbu

1. Pievienota moduļa dokumentācijas rinda (faila galvenē).
   Tagad ir skaidrs, ko modulis dara. Norādīts, ka to var importēt citās programmās.

2. Pievienoju importu `from typing import List`.
   Iespēja izmantot tipu norādes (type hints). IDE tagad var pārbaudīt datu tipu pareizību.

3. Pievienoju tipu norādes (type hints) `__init__` metodē.
   Kods kļuva pašdokumentējošs. `dati: List[float]` - skaidri norādīts, ka parametram `dati` jābūt skaitļu sarakstam; `-> None` - norādīts, ka metode neko neatgriež.

4. Paplašināju `__init__` metodes docstring.
   Parametra `Args` apraksts - kas jānodod metodē, un `Raises` apraksts - kādu kļūdu metode var izraisīt un kad.

5. Pievienoju tukša saraksta kļūdas apstrādi.
   Programma nemēģinās dalīt ar nulli, aprēķinot vidējo vērtību, un lietotājs saņems saprotamu kļūdas paziņojumu.

### Rezultāts

[`vng04_funkcijas.py`](./pielikumi/vng04_funkcijas.py)

```python id="p62h2r"    
"""Šis modulis satur klasi SvaruAnalizators, kas aprēķina
kopējo un vidējo svaru no datu saraksta. Moduli var
importēt un izmantot citās programmās."""

from typing import List
class SvaruAnalizators:
    """Analizē atradumu svarus un veic nepieciešamos aprēķinus."""
    
    def __init__(self, dati: List[float]) -> None:
        """Inicializē analizatoru ar datu sarakstu.
        Args:
            dati: Skaitļu saraksts (atradumu svari gramos)
        Raises:
            ValueError: Ja datu saraksts ir tukšs
        """
        if not dati:
            raise ValueError("Datu saraksts nedrīkst būt tukšs")
        self.dati = dati
    
    def kopejais_svars(self):
        """Aprēķina un atgriež kopējo svaru."""
        return sum(self.dati)
    
    def videjais_svars(self):
        """Aprēķina un atgriež vidējo svaru."""
        return sum(self.dati) / len(self.dati)
    
    def izvadit(self):  # ← Теперь внутри класса (с отступом)
        """Izvada aprēķinu rezultātus konsolē."""
        print("\nKopējais svars:", self.kopejais_svars())
        print("Vidējais svars:", self.videjais_svars())
        print()

# Programmas palaišana
if __name__ == "__main__":
    dati = [15, 120, 30, 250, 12]
    analizators = SvaruAnalizators(dati)
    analizators.izvadit()
```
---

## 5.2 Uzdevums 5

Nepieciešams analizēt sākotnējo programmu pēc loģikas un atbilstības 
PEP 8 komentāru rakstīšanas noteikumiem, kā arī izlabot kodu:

```python id="p62h2r"  
atradumu_skaits = 0

atradumu_skaits = atradumu_skaits + 1  # Pieskaita viens
print(atradumu_skaits)  # Izvada atradumu skaitu

if atradumu_skaits > 0:
    print("Ir atradumi")  # Izvada tekstu
    print("Nav atradumu")
```

### Ko darīju

Es analizēju sākotnējā koda loģiku un atklāju, ka skaitītājam šajā programmā 
nav jēgas, jo vērtība tiek noteikta jau sākotnēji. Tāpat es analizēju komentārus 
pēc nepieciešamības un liekuma kritērijiem, saskaņā ar PEP 8 noteikumiem.

### Kā veicu darbu

1. Noņēmu skaitītāju - atradumu_skaits = atradumu_skaits + 1, jo stingri 
   noteiktā mainīgā vērtība padara skaitītāja palielināšanu bezjēdzīgu.

2. Izlaboju izvades loģiku - pievienoju else zaru gadījumam, kad atradumu 
   nav (mainīgā vērtība ir 0).

3. Izdzēsu liekos komentārus - noņēmu komentārus, kas izskaidroja acīmredzamu 
   sintaksi.

4. Pievienoju vienīgo nepieciešamo komentāru - noformēju to kā docstring ar 
   trīskārtīgām pēdiņām, kas izskaidro programmas mērķi, nevis tās acīmredzamo 
   sintaksi un loģiku.

### Rezultāts

[`vng02_komentari.py`](./pielikumi/vng02_komentari.py)

```python id="p62h2r"    
"""Programmas loģika, lai paziņotu arheologam, vai attiecīgajā vietā
ir atradumi un cik to ir.
"""

atradumu_skaits = 2

# atradumu_skaits = atradumu_skaits + 1
#print(atradumu_skaits)

if atradumu_skaits > 0:
    print("Ir atradumi")
    print(atradumu_skaits)
else:    
    print("Nav atradumu")
```
---

## 5.2 Uzdevums 6

Izveidojiet programmu svara aprēķināšanai, izmantojot šādas funkcijas:

```python id="p62h2r"  
def nolasit_datus():
def aprekinat_kopejo_svaru(dati):
def aprekinat_videjo_svaru(dati):
def paradit_rezultatu(kopejais_svars, videjais_svars):
def main():
```
Sagatavot programmas dokumentāciju saskaņā ar PEP 8 vadlīnijām.

### Ko darīju

Es analizēju sākotnējā koda loģiku un atklāju, ka skaitītājam šajā programmā 
nav jēgas, jo vērtība tiek noteikta jau sākotnēji. Tāpat es analizēju komentārus 
pēc nepieciešamības un liekuma kritērijiem, saskaņā ar PEP 8 noteikumiem.

### Kā veicu darbu

1. Pievienoju pilnu dokumentāciju - moduļa sākumā, klasei, katrai metodei un funkcijām, izmantojot docstring 
2. formātu ar parametru, atgriežamo vērtību un iespējamo kļūdu aprakstiem.
   noteiktā mainīgā vērtība padara skaitītāja palielināšanu bezjēdzīgu.

3. Ieviesu datu tipu pārbaudi - pievienoju importu from typing import List un tipu norādes visām metodēm, kas 
4. padara kodu pašdokumentējošu un ļauj IDE pārbaudīt lietošanas pareizību.

5. Pievienoju aizsardzību pret nekorektiem datiem - klases konstruktorā ieviesu divas pārbaudes:
   * Tukša saraksta pārbaudi (izmet ValueError)
   * Katra elementa pārbaudi, lai pārliecinātos, ka visas vērtības ir skaitļi (izmet TypeError)

6. Organizēju kodu loģiskos blokos:
   * Funkcija nolasit_datus() - atbild par datu iegūšanu
   * Funkcija main() - vada programmas loģiku
   * Klase SvaruAprekins - veic aprēķinus
   * Bloks if __name__ == "__main__" - ļauj moduli izmantot gan neatkarīgi, gan importēt citās programmās

7. Pievienoju kļūdu apstrādi - funkcijā main() izmantota try/except konstrukcija ValueError kļūdas uztveršanai, 
   kas novērš programmas avārijas apstāšanos, ja datu saraksts ir tukšs.

### Rezultāts

[`pd17_gala_versija.py`](./pielikumi/pd17_gala_versija.py)

```python id="p62h2r"    
"""Šis modulis satur klasi SvaruAprekins, kas aprēķina
kopējo un vidējo svaru no datu saraksta. Moduli var
importēt un izmantot citās programmās."""

from typing import List

class SvaruAprekins:
    """Analizē atradumu svarus un veic nepieciešamos aprēķinus."""
    
    def __init__(self, dati: List[float]) -> None:
        """Inicializē analizatoru ar datu sarakstu.
        Args:
            dati: Skaitļu saraksts (atradumu svari gramos)
        Raises:
            ValueError: Ja datu saraksts ir tukšs
        """
        if not dati:
            raise ValueError("Datu saraksts nedrīkst būt tukšs")
    
        # Katra elementa pārbaude, vai tas ir skaitlis
        for svars in dati:
            if not isinstance(svars, (int, float)):
                raise TypeError(f"'{svars}' nav skaitlis!")
    
        self.dati = dati

    def aprekinat_kopejo_svaru(self):
        """Aprēķina un atgriež kopējo svaru."""
        return sum(self.dati)
    
    def aprekinat_videjo_svaru(self):
        """Aprēķina un atgriež vidējo svaru."""
        return sum(self.dati) / len(self.dati)
    
    def paradit_rezultatu(self):  
        """Izvada aprēķinu rezultātus konsolē."""
        print("\nAtradumu skaits:", len(self.dati))
        print("Kopējais svars:", float(self.aprekinat_kopejo_svaru()))
        print("Vidējais svars:", self.aprekinat_videjo_svaru())
        print()


def nolasit_datus():
    """Nolasa datus no sagatavota saraksta.
    
    Returns:
        List[float]: Skaitļu saraksts (svari gramos)
    """
    # Datu saraksts atbilstoši uzdevuma prasībai
    atradumu_svari = [15, 120, 30, 250, 12]
    return atradumu_svari


def main():
    """Galvenā programmas funkcija - vada programmas darbību."""
    svari = nolasit_datus()
    
    # Kļūdas apstrāde tukšā sarakstā
    try:
        analizators = SvaruAprekins(svari)
        analizators.paradit_rezultatu()
    except ValueError as e:
        print(f"\nKļūda: {e}\n")

# Programmas palaišana
if __name__ == "__main__":
    main()
```
---

# 6. Atrastās problēmas un novērojumi

| Problēma vai novērojums | Iespējamā ietekme |
| ----------------------- | ----------------- |
| 1. uzdevumā tika identificēti maģiskie skaitļi | Kods kļūst nelasāms un grūti uzturējams|
| 2. uzdevumā programmas loģika ir bojāta | Nepareiza rezultātu izvade |
| 3. uzdevumā trūka funkciju un dokumentācijas| Kods nav atkārtoti izmantojams, saprotams, grūti testējams un labojams |
| 3. un 4. uzdevumā trūkst datu validācijas |  Var izraisīt programmas avāriju. |

---

# 7. Veiktās izmaiņas

Uzdevumu gaitā tika veiktas izmaiņas

| Izmaiņa | Pamatojums |
|---------|------------|
| Pārdēvēti mainīgie: `x` → `atradumu_skaits`, `y` → `kopējais_svars`, `z` → `vecākais_vecums` | Lai mainīgo nosaukumi būtu saprotami un atbilstu PEP 8 snake_case standartam. Tas uzlabo koda lasāmību un uzturēšanu. |
| Pievienotas trīs funkcijas: `nolasit_datus()`, `analizet_datus()`, `paradit_rezultatu()` | Lai kods būtu modulārs, atkārtoti izmantojams un vieglāk testējams. Katra funkcija veic vienu konkrētu uzdevumu. |
| Pievienoti docstring un noņemti lieki komentāri | Lai dokumentācija izskaidrotu **kāpēc**, nevis **ko** dara kods. Docstring ir pieejami caur `help()`. |
| Pievienota datu validācija: pārbaude vai saraksts nav tukšs | Lai programma neavarētu, mēģinot dalīt ar nulli, aprēķinot vidējo vērtību. |
| Pievienota kļūdu apstrāde (`try/except`) funkcijā `main()` | Lai lietotājs saņemtu saprotamu kļūdas paziņojumu, nevis nesaprotamu programmas avāriju. |
| Pievienots bloks `if __name__ == "__main__"` | Lai moduli varētu gan importēt citās programmās, gan palaist neatkarīgi. |
| Pievienota tipu norāde (`from typing import List`) | Lai kods būtu pašdokumentējošs un IDE varētu pārbaudīt datu tipu pareizību. |

---

# 8. Uzturēšanas analīze

### Kāda veida uzturēšana tika veikta?

✅ **Corrective (koriģējošā)**

☐ Adaptive (adaptīvā)

✅ **Perfective (pilnveidojošā)** 

☐ Preventive (profilaktiskā)** 

Pamatojums:
Обоснование:

---

PD17 projektā tika veikti **divi uzturēšanas veidi**:

**1. Korektīvā uzturēšana** (kļūdu labošana):
- 2. vingrinājumā tika atklāta un izlabota loģikas kļūda - noņemts bezjēdzīgais skaitītājs `atradumu_skaits = atradumu_skaits + 1`, kam nebija loģiska pamatojuma

**2. Pilnveidojošā uzturēšana** (koda uzlabošana):
- Mainīgie pārdēvēti uz saprotamiem nosaukumiem (snake_case)
- Komentāri pārveidoti, lai izskaidrotu "kāpēc", nevis "ko"
- Kods sadalīts funkcijās
- Pievienoti docstring
- Izveidota projekta dokumentācija (README.md)

Abi uzturēšanas veidi tika veikti, lai uzlabotu programmas kvalitāti un novērstu esošās problēmas.
---

### Vai tika identificēts tehniskais parāds?

✅ **Jā**

☐ Nē

---

Jā, projektā tika identificēts tehniskais parāds. Sākotnējā programmā pastāvēja vairākas problēmas, kas kavēja tālāku attīstību un uzturēšanu:

| Problēma | Tehniskā parāda veids |
|----------|----------------------|
| Neskaidri mainīgo nosaukumi (x, y, z) | Lasāmības parāds |
| Trūkst funkciju, viss kods ir lineārs | Strukturālais parāds |
| Lieki komentāri, kas izskaidro acīmredzamu sintaksi | Dokumentācijas parāds |
| Trūkst docstring | Dokumentācijas parāds |
| Nav datu validācijas un kļūdu apstrādes | Kvalitātes parāds |
| Bezjēdzīgs skaitītājs, kas pārkāpj loģiku | Loģikas parāds |

**KTehniskā parāda samazināšana:**

- Mainīgie pārdēvēti uz saprotamiem nosaukumiem
- Kods sadalīts funkcijās
- Pievienoti docstring un noderīgi komentāri
- Pievienota datu validācija un kļūdu apstrāde
- Noņemts bezjēdzīgais skaitītājs

---

### Incidenti pēc pieprasījuma un pēc izmaiņām

☐ Incident / Инцидент

☐ Change Request / Запрос на изменение

✅ **Abi / Оба**

---

### Pamatojums / Обоснование

**Latviski:**

Projektā tika konstatēti gan **incidents**, gan **izmaiņu pieprasījums**.

**1. Incidents (kļūda programmā):**
- 2.vingrinājumā tika atklāta loģikas kļūda - bezjēdzīgais skaitītājs `atradumu_skaits = atradumu_skaits + 1`
- Šī kļūda ietekmēja programmas loģiku, lai gan programma formāli darbojās
- Kļūda tika izlabota, noņemot bezjēdzīgo skaitītāju

**2. Izmaiņu pieprasījums (uzlabojuma pieprasījums):**
- Visā PD17 projektā tika pieprasītas izmaiņas koda kvalitātes uzlabošanai:
  - Pārdēvēt mainīgos uz saprotamiem nosaukumiem (snake_case)
  - Pārveidot komentārus (kāpēc, nevis ko)
  - Sadalīt kodu funkcijās
  - Pievienot docstring
  - Izveidot projekta dokumentāciju (README.md)

Abi gadījumi prasīja izmaiņas esošajā kodā - gan kļūdas labojumu, gan koda uzlabojumus.

---

# 9. Rezultāts
  9. Результат

Apraksti gala rezultātu.
Опиши итоговый результат.


Uzlabots:
- Mainīgo nosaukumi pārdēvēti uz saprotamiem (snake_case)
- Kods sadalīts funkcijās (modularitāte)
- Pievienota datu validācija un kļūdu apstrāde
- Pievienota tipu norāde (type hints)
- Izveidota projekta dokumentācija (README.md)

Fiksēts:
- Noņemts bezjēdzīgais skaitītājs, kas pārkāpa programmas loģiku
- Izdzēsti lieki komentāri, kas izskaidroja acīmredzamu sintaksi
- Pievienota pārbaude tukšam sarakstam (novērsta dalīšana ar nulli)

Tas tika dokumentēts:
- Pievienots docstrings katrai funkcijai
- Pievienots moduļa apraksts (faila sākumā)
- Izveidots README.md ar projekta aprakstu un instrukcijām
- Izveidots vng05_projekta_struktura.txt ar mapju struktūru

Ieguvumi lietotājam vai projekta uzturētājam:

| Saņēmējs | Ieguvums |
|----------|----------|
| **Lietotājs** | Programma ir drošāka - tā neavar ar nederīgiem datiem. Lietotājs saņem saprotamus kļūdas paziņojumus. |
| **Uzturētājs** | Kods ir vieglāk saprotams, labojams un paplašināms. Dokumentācija palīdz ātri orientēties projektā. Moduļu struktūra ļauj atkārtoti izmantot funkcijas citos projektos. |

---

# 10. Problēmas un to risinājumi

### Problēma

Bezjēdzīgs skaitītājs programmas loģikā

### Kā izpaudās

Sākotnējā programmā bija rinda atradumu_skaits = atradumu_skaits + 1. Šim skaitītājam nebija loģiska pamatojuma, jo mainīgā vērtība tika noteikta iepriekš (atradumu_skaits = 2). Programma formāli darbojās, bet saturēja neloģisku kodu, kas varēja maldināt citus programmētājus un apgrūtināt koda uzturēšanu.

### Kā atrisināju

Es rūpīgi analizēju programmas loģiku un sapratu, ka skaitītājs nav vajadzīgs. Tāpēc es:

1. Noņēmu bezjēdzīgo rindu atradumu_skaits = atradumu_skaits + 1

2. Atstāju tikai loģiski pareizo kodu ar nosacījumu if/else

3. Pievienoju komentāru, kas izskaidro kāpēc programma pārbauda atradumu skaitu

### Ko iemācījos

* Analizēt koda loģiku pirms veikt izmaiņas

* Atpazīt bezjēdzīgus koda fragmentus, kas tikai apgrūtina lasāmību

* Nepietiek, ka programma darbojas - tai jābūt arī loģiski pareizai

* Komentēt "kāpēc", nevis "ko" - lai citi saprastu domāšanas procesu

* Viens no svarīgākajiem principiem: labs kods nav tikai tas, kas darbojas šodien.   Tam jābūt saprotamam arī pēc mēneša vai gada.

---

# 11. Secinājumi

- **Kods jāraksta cilvēkam, nevis tikai datoram** - tam jābūt lasāmam un saprotamam
- **Skaidri mainīgo nosaukumi (snake_case)** ir ļoti svarīgi koda lasāmībai
- **Komentāriem jāatbild uz "kāpēc"**, nevis "ko" dara kods
- **Funkcijas palīdz sadalīt kodu mazākās, pārvaldāmās daļās**
- **Docstring ir oficiālā dokumentācija**, kas pieejama caur `help()`
- **Datu validācija un kļūdu apstrāde** padara programmu drošāku
- **Tehniskais parāds** ir reāla problēma, kas jāsamazina
- **README.md** ir pirmais, ko lasa citi programmētāji

---

# 12. Pašvērtējums

## Pašvērtējuma tabula

| Kritērijs | Maks. punkti | Mani punkti | Pamatojums |
|-----------|--------------|-------------|------------|
| **Analīzes kvalitāte** | 25 | 23 | Kods tika rūpīgi analizēts. Atrastas visas galvenās problēmas: neskaidri mainīgie, lieki komentāri, trūkstošas funkcijas, datu validācijas trūkums. |
| **Problēmu identificēšana** | 25 | 24 | Identificētas 6 problēmas: neskaidri nosaukumi, bezjēdzīgs skaitītājs, lieki komentāri, trūkstošas funkcijas, dokumentācijas trūkums, datu validācijas trūkums. |
| **Izmaiņu pamatojums** | 25 | 23 | Katrai izmaiņai ir skaidrs pamatojums (lasāmība, modularitāte, drošība, dokumentācija). Viss pamatots ar PEP 8 standartiem un labas prakses principiem. |
| **Dokumentēšana** | 15 | 14 | Pievienoti docstring katrai funkcijai, moduļa apraksts, izveidots README.md un projekta struktūras fails. |
| **Atskaite** | 10 | 10 | Atskaite ir pilnīga, satur visus nepieciešamos punktus: problēmas, risinājumus, secinājumus, pašvērtējumu. Pievienoti ekrānuzņēmumi. |
| **Kopā** | **100** | **94** | |

---

## Komentārs

Atņemtie 6 punkti (pa 2 punktiem no analīzes kvalitātes, izmaiņu pamatojuma un dokumentēšanas), jo:

- Analīzē varēja vēl dziļāk izpētīt katra koda fragmenta ietekmi uz kopējo projektu
- Dažas izmaiņas varēja pamatot ar vairāk piemēriem no reālas prakses
- Dokumentācijā varēja pievienot vēl detalizētākus piemērus koda lietošanai

---

# 13. Pielikumi

Materiāli ir pievienoti

* projekta faili - /PD17/pielikumi/*.*; 
* ekrānattēli - /PD17/atteli/*.*;
* dokumentācija - READMI.md, atskaite_PD17.md, vng05_projekta_struktura.txt; 
* [Git izmaiņu vēsture](https://github.com/JanTey/Python_Course/blob/main/PD17/atskaite_PD17.md).
