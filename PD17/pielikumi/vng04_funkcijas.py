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
