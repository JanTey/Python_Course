import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
Izveido programmu ar Tkinter logu, kas analizē failu atradumi.csv.
Programmai jābūt pogai:
    Analizēt datus
Kad lietotājs nospiež pogu, programma nolasa failu un parāda logā:
 - atradumu skaitu
 - kopējo svaru
 - vidējo svaru
 - vecākā atraduma nosaukumu
 - vecākā atraduma vecumu
Sagaidāmais rezultāts
Piemērs:
    Atradumu skaits: 5
    Kopējais svars: 427 g
    Vidējais svars: 85.4 g
    Vecākais atradums: Keramikas gabals
    Vecums: 1200 gadi
Ja fails nav atrasts, logā jāparādās kļūdas paziņojumam:
    Kļūda: fails nav atrasts!
"""
import ttkbootstrap as tb
import ttkbootstrap.constants as tbs
import os

class Analizators:
    # Klase arheoloģisko atradumu analizēšanai
    
    def __init__(self):
        #Konstruktors - izveido logu un visus elementus
        
        # Loga izmēri
        self.platums = 500
        self.augstums = 450
        
        # Izveido galveno logu ar tumšo tēmu
        self.logs = tb.Window(
            themename="darkly", 
            title="PD16 - Arheoloģisko atradumu analizators", 
            size=(self.platums, self.augstums)
        )
        
        # Centrē logu uz ekrāna
        self.logs.eval('tk::PlaceWindow . center')
        self.logs.resizable(True, True)
        
        # Izveido rāmi elementu izvietošanai
        self.frame = tb.Frame(self.logs, padding=20)
        self.frame.pack(fill=tbs.BOTH, expand=tbs.YES)
        
        # Konfigurē kolonnu, lai tā izstieptos
        self.frame.columnconfigure(0, weight=1)
        
        # Loga virsraksts (etiķete)
        self.etikete = tb.Label(
            self.frame, 
            text="Arheoloģisko atradumu analizators", 
            font=("Arial", 16, "bold"),
            anchor="center"
        )
        self.etikete.grid(row=0, column=0, pady=30, sticky="ew")
        
        # Poga datu analīzei
        self.poga = tb.Button(
            self.frame, 
            text="Analizēt datus", 
            command=self.analizet_datus,
            bootstyle="primary",
            width=25
        )
        self.poga.grid(row=1, column=0, pady=20)
        
        # Etiķete rezultāta parādīšanai (bez fona laukuma)
        self.rezultats = tb.Label(
            self.frame, 
            text="", 
            font=("Courier", 15),
            anchor="w",  # Piestiprina tekstu pie kreisās malas
            justify="left"  # Teksta izlīdzinājums pa kreisi
        )
        self.rezultats.grid(row=2, column=0, pady=20, sticky="w")
        self.centret_logu()  # <--- IZSAUKUMS    
    def analizet_datus(self):
        """Metode, kas nolasa CSV failu un veic datu analīzi"""
        
        # Meklē faila ceļu - vispirms tajā pašā mapē, tad Pielikumi mapē
        skripta_mape = os.path.dirname(os.path.abspath(__file__))
        faila_cels = os.path.join(skripta_mape, "atradumi.csv")
        
        # Ja fails nav atrasts, meklē Pielikumi apakšmapē
        if not os.path.exists(faila_cels):
            faila_cels = os.path.join(skripta_mape, "Pielikumi", "atradumi.csv")
        
        try:
            # Atver un nolasa failu
            with open(faila_cels, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            # Apstrādā datus - izlaiž pirmo rindu (virsrakstus)
            dati = []
            for line in lines[1:]:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        nosaukums = parts[0].strip()
                        svars = float(parts[1].strip())
                        vecums = float(parts[2].strip())
                        dati.append({
                            "nosaukums": nosaukums,
                            "svars": svars,
                            "vecums": vecums
                        })
            
            # Pārbauda, vai dati ir veiksmīgi nolasīti
            if not dati:
                self.rezultats.config(text="Kļūda: fails ir tukšs vai nav pareizi formatēts!")
                return
            
            # 1. Aprēķina atradumu skaitu
            skaits = len(dati)
            
            # 2. Aprēķina kopējo svaru
            kop_svars = sum(atradums["svars"] for atradums in dati)
            
            # 3. Aprēķina vidējo svaru
            vid_svars = kop_svars / skaits
            
            # 4. Atrast vecāko atradumu (ar lielāko vecumu)
            vecakais = max(dati, key=lambda x: x["vecums"])
            
            # Izveido rezultāta tekstu
            rezultata_teksts = f"""Atradumu skaits: {skaits}
Kopējais svars: {int(kop_svars)} g
Vidējais svars: {vid_svars:.1f} g
Vecākais atradums: {vecakais["nosaukums"]}
Vecums: {int(vecakais["vecums"])} gadi"""
            
            # Parāda rezultātu logā
            self.rezultats.config(text=rezultata_teksts)
            
        except FileNotFoundError:
            # Kļūdas paziņojums, ja fails nav atrasts
            self.rezultats.config(text="Kļūda: fails nav atrasts!")
        except Exception as e:
            # Citu kļūdu apstrāde
            self.rezultats.config(text=f"Kļūda: {str(e)}")
    
    def palaist(self):
        """Palaiž programmas galveno ciklu"""
        self.logs.mainloop()
    
    def centret_logu(self):
        self.logs.update_idletasks()
        x = (self.logs.winfo_screenwidth() // 2) - (self.platums // 2)
        y = (self.logs.winfo_screenheight() // 2) - (self.augstums // 2)
        self.logs.geometry(f"{self.platums}x{self.augstums}+{x}+{y}")

# Programmas palaišana
if __name__ == "__main__":
    app = Analizators()
    app.palaist()