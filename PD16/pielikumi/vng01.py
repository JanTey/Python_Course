import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
** Uzdevums
Izveido pirmo Tkinter programmu.
Programmai jāatver logs ar:
 - nosaukumu PD16 — Mans pirmais logs
 - izmēru 350x150
Logā pagaidām nav jābūt pogām vai ievades laukiem.
** Sagaidāmais rezultāts
Atveras tukšs logs ar norādīto nosaukumu.
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
            title="PD16 — Mans pirmais logs", 
            size=(self.platums, self.augstums)
        )
        
        # Centrē logu
        self.logs.eval('tk::PlaceWindow . center')
        
        # Iestatījumi
        self.logs.resizable(True, True)
        self.logs.focus_force()
    
    def palaist(self):
        self.logs.mainloop()

# Palaišana
if __name__ == "__main__":
    app = MansPirmaisLogs()
    app.palaist()