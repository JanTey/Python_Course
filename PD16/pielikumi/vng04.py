import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
Izveido programmu, kas aprēķina divu skaitļu summu.
Programmai jābūt:
 - pirmajam ievades laukam
 - otrajam ievades laukam
 - pogai Saskaitīt
 - rezultāta laukam
Ja lietotājs ievada nepareizus datus, programma nedrīkst sabrukt. Tā vietā jāparāda
paziņojums:
 Kļūda: ievadi skaitļus!
Sagaidāmais rezultāts
Piemērs:
 Pirmais skaitlis: 12
 Otrais skaitlis: 8
 Rezultāts: 20
"""
import ttkbootstrap as tb
from tkinter import messagebox
import ttkbootstrap.constants as tbs 

class SummaProgramma:
    def __init__(self):
        # Loga iestatījumi
        self.platums = 320
        self.augstums = 200
        
        # Izveidojiet logu
        self.logs = tb.Window(
            themename="darkly", 
            title="Saskatītājs", 
            size=(self.platums, self.augstums)
        )
        
        # Centrēt logu
        self.logs.eval('tk::PlaceWindow . center')
        
        # Izveidojiet rāmi elementu organizēšanai
        self.frame = tb.Frame(self.logs, padding = 20)
        self.frame.pack(fill=tbs.BOTH, expand=tbs.YES)
        
        # Teksta etiķete
        self.etikete1 = tb.Label(self.frame, text="Pirmais skaitlis:", font=("Arial", 14))
        self.etikete1.grid(row=0, column=0, pady=5, sticky="e")
        
        # Ievades lauks (Entry)
        self.ievades_lauks1 = tb.Entry(self.frame, width = 20, font = ("Arial", 14))
        self.ievades_lauks1.grid(row=0, column=1, pady=5, padx=5)
        
        self.etikete2 = tb.Label(self.frame, text="Otrais skaitlis:", font=("Arial", 14))
        self.etikete2.grid(row=2, column=0, pady=5, sticky="e")
        
        # Ievades lauks (Entry)
        self.ievades_lauks2 = tb.Entry(self.frame, width = 20, font = ("Arial", 14))
        self.ievades_lauks2.grid(row=2, column=1, pady=5, padx=5)        
        
        
        # Poga (Button)
        self.poga = tb.Button(
            self.frame, 
            text = "Saskaitīt", 
            command = self.paradit_skaitit,  # Klases metodes izsaukšana
            bootstyle = "success"
        )
        self.poga.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Rezultāta izvades etiķete
        self.rezultats = tb.Label(self.frame, text = "", font = ("Arial", 16, "bold"))
        self.rezultats.grid(row=5, column=0, columnspan=2, pady=10)
        
    def paradit_skaitit(self):
        try:
            skaitlis1 = float(self.ievades_lauks1.get())  
            skaitlis2 = float(self.ievades_lauks2.get())  
            summa = skaitlis1 + skaitlis2

            self.rezultats.config(text=f"Rezultāts:  {summa:.2f}")
        
        except ValueError:
        # Ja tiek ievadīti neskaitļi
            self.rezultats.config(text="Kļūda: ievadi skaitļus!")    
    
    def palaist(self):
        self.logs.mainloop()

# Programmas palaišana
if __name__ == "__main__":
    app = SummaProgramma()
    app.palaist() 