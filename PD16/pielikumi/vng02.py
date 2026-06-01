import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
Izveido Tkinter logu, kurā redzama teksta etiķete:
 Sveiks! Šī ir mana pirmā GUI programma.
Izvieto tekstu ar .grid() metodi.
Sagaidāmais rezultāts
Logā redzams teksts.
"""
import ttkbootstrap as tb

class MansPirmaisLogs:
    def __init__(self):
        # Loga iestatījumi
        self.platums = 350
        self.augstums = 150
        
        # Izveido logu
        self.logs = tb.Window(
            themename="darkly", 
            title="Teksta parādišāna", 
            size=(self.platums, self.augstums)
        )
        
        # Centrē logu
        self.logs.eval('tk::PlaceWindow . center')
        
        # Iestatījumi
        self.logs.resizable(True, True)
        self.logs.focus_force()
        
        teksts = tb.Label(
            self.logs, 
            text="Sveiks! Šī ir mana pirmā GUI programma.",
            font=("Arial", 12)
        )
        
        # Ievietojiet etiķeti logā, izmantojot .grid()
        teksts.grid(row=0, column=0, padx=20, pady=20)
    
    def palaist(self):
        self.logs.mainloop()

# Palaišana
if __name__ == "__main__":
    app = MansPirmaisLogs()
    app.palaist()
