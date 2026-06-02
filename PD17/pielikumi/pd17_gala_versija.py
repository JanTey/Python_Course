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