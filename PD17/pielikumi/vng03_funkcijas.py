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
        print("\nKopējais svars:", self.kopejais_svars())
        print("Vidējais svars:", self.videjais_svars(), "\n")

# Programmas palaišana
if __name__ == "__main__":
    dati = [15, 120, 30, 250, 12]
    analizators = SvaruAnalizators(dati)
    analizators.izvadit()
