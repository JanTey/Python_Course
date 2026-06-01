import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
Izveido klasi Kruze.
Sākumā krūze ir tukša.
Klasei jābūt:
atribūtam piepildita
metodei ieliet()
metodei izdzert()
metodei paradit_stavokli()
Programmai jāparāda, kā krūzes stāvoklis mainās.
Uzdevums
Izveido programmu, kurā lietotājs ievada savu vārdu.
Programmai jābūt:
 - ievades laukam
 - pogai Parādīt sveicienu
 - rezultāta tekstam
Kad lietotājs nospiež pogu, logā jāparādās sveicienam.
Sagaidāmais rezultāts
Piemērs:
 Ievadiet vārdu: Anna
 Sveiki, Anna!
"""
import ttkbootstrap as tb
from tkinter import messagebox
import ttkbootstrap.constants as tbs 

class SveicienaProgramma:
    def __init__(self):
        # Loga iestatījumi
        self.platums = 320
        self.augstums = 200
        
        # Izveidojiet logu
        self.logs = tb.Window(
            themename="darkly", 
            title="Sveiciena programma", 
            size=(self.platums, self.augstums)
        )
        
        # Centrēt logu
        self.logs.eval('tk::PlaceWindow . center')
        
        # Izveidojiet rāmi elementu organizēšanai
        self.frame = tb.Frame(self.logs, padding = 20)
        self.frame.pack(fill=tbs.BOTH, expand=tbs.YES)
        
        # Teksta etiķete
        self.etikete = tb.Label(self.frame, text="Ievadiet vārdu:", font=("Arial", 14))
        self.etikete.grid(row=0, column=0, pady=5, sticky="e")
        
        # Ievades lauks (Entry)
        self.ievades_lauks = tb.Entry(self.frame, width = 20, font = ("Arial", 14))
        self.ievades_lauks.grid(row=0, column=1, pady=5, padx=5)
        
        # Poga (Button)
        self.poga = tb.Button(
            self.frame, 
            text = "Parādīt sveicienu", 
            command = self.paradit_sveicienu,  # Klases metodes izsaukšana
            bootstyle = "success"
        )
        self.poga.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Rezultāta izvades etiķete
        self.rezultats = tb.Label(self.frame, text = "", font = ("Arial", 16, "bold"))
        self.rezultats.grid(row=2, column=0, columnspan=2, pady=10)
        
    def paradit_sveicienu(self):
        # Metode, kas tiek izsaukta, noklikšķinot uz pogas
        vards = self.ievades_lauks.get()  # Teksta iegūšana no ievades lauka
        
        if vards:  # Ja lauks nav tukšs
            self.rezultats.config(text=f"Sveiki, {vards}!")  # Sveiciena rādīšana
        else:
            self.rezultats.config(text="Lūdzu, ievadiet vārdu!")  # Kļūdas ziņojums
    
    def palaist(self):
        self.logs.mainloop()

# Programmas palaišana
if __name__ == "__main__":
    app = SveicienaProgramma()
    app.palaist() 