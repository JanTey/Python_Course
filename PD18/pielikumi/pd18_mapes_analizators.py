import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()

"""
Gala programma PD18 ar Tkinter logu — Mapes analizators un projekta kvalitātes pārbaudītājs.
Izmanto funkcijas no vng04.py, vng05.py, vng06.py.
"""

import os
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import subprocess

# Importē jau esošās funkcijas
from vng04 import check_items as parbaudit_elementus
from vng05 import check_for_spaces as parbaudit_nosaukumus
from vng06 import count_files_by_type as skaitit_failus


def get_folder_stats(directory):
    """
    Analizē norādīto mapi, izmantojot esošās funkcijas.
    
    Parametri
    ---------
    directory : str
        Ceļš uz mapi, kuru analizēt
    
    Atgriež
    -------
    dict
        Vārdnīca ar analīzes rezultātiem
    """
    # Pārbauda, vai mape eksistē
    if not os.path.exists(directory):
        return None
    
    # 1. Savāc informāciju par mapēm un failiem (izmantojot os.walk)
    total_files = 0
    total_folders = 0
    
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            total_folders += 1
        for f in files:
            total_files += 1
    
    # 2. Izmanto esošo funkciju no vng06.py failu skaitīšanai
    file_counts = skaitit_failus(directory)
    
    # 3. Pārbauda obligātās mapes (izmantojot os.path, jo vng04 tikai izvada)
    pielikumi_exists = os.path.exists(os.path.join(directory, 'Pielikumi')) and os.path.isdir(os.path.join(directory, 'Pielikumi'))
    atteli_exists = os.path.exists(os.path.join(directory, 'atteli')) and os.path.isdir(os.path.join(directory, 'atteli'))
    
    # 4. Pārbauda atstarpes nosaukumos (izmantojot esošo funkciju no vng05.py)
    # Piezīme: funkcija parbaudit_nosaukumus izvada rezultātu, bet arī atgriež sarakstu
    files_with_spaces = parbaudit_nosaukumus(directory)
    
    return {
        'exists': True,
        'total_files': total_files,
        'total_folders': total_folders,
        'python_files': file_counts.get('python', 0) if file_counts else 0,
        'markdown_files': file_counts.get('markdown', 0) if file_counts else 0,
        'image_files': file_counts.get('images', 0) if file_counts else 0,
        'pielikumi_exists': pielikumi_exists,
        'atteli_exists': atteli_exists,
        'files_with_spaces': files_with_spaces if files_with_spaces else []
    }


def format_results(result, directory):
    """
    Formatē analīzes rezultātus lasāmā tekstā.
    """
    if result is None:
        return f"❌ KĻŪDA: Mape '{directory}' neeksistē!"
    
    output = ""
    output += "=" * 50 + "\n"
    output += "PROJEKTA PĀRBAUDES ATSKAITE\n"
    output += "=" * 50 + "\n\n"
    
    # Mapes esamība
    output += "✓ Mape eksistē\n"
    
    # Obligātās mapes
    if result['pielikumi_exists']:
        output += "✓ Mape Pielikumi atrasta\n"
    else:
        output += "✗ Mape Pielikumi nav atrasta\n"
    
    if result['atteli_exists']:
        output += "✓ Mape atteli atrasta\n"
    else:
        output += "✗ Mape atteli nav atrasta\n"
    
    output += "\n"
    
    # Failu un mapju skaits
    output += f"Failu skaits: {result['total_files']}\n"
    output += f"Mapju skaits: {result['total_folders']}\n"
    output += f"Python faili: {result['python_files']}\n"
    output += f"Attēlu faili: {result['image_files']}\n"
    
    output += "\n"
    
    # Brīdinājumi par atstarpēm nosaukumos
    output += "Brīdinājumi:\n"
    if result['files_with_spaces']:
        for file_path in result['files_with_spaces']:
            output += f"⚠ Faila nosaukumā atrasta atstarpe:\n   {file_path}\n"
    else:
        output += "Nav atrasti faili ar atstarpēm nosaukumos.\n"
    
    output += "\n"
    output += "=" * 50 + "\n"
    output += "Pārbaude pabeigta.\n"
    output += "=" * 50
    
    return output


class ProjektAnalizators:
    """
    Tkinter loga klase projekta analīzei.
    """
    
    def __init__(self):
        """Inicializē Tkinter logu un visus elementus."""
        self.root = tk.Tk()
        
        
        
        self.root.title("PD18 — Mapes analizators")
        self.root.geometry("750x650")
        self.root.resizable(True, True)
        
        # self.root.attributes('-topmost', True)
        # self.root.lift()
        self.root.focus_force()
          
        # Galvenais rāmis
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Virsraksts
        title_label = tk.Label(
            main_frame, 
            text="PROJEKTA PĀRBAUDES ATSKAITE", 
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=(0, 12))
        
        # Ievades rāmis
        input_frame = tk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 12))
        
        # Ievades lauks
        tk.Label(input_frame, text="Mapes ceļš:").pack(side=tk.LEFT, padx=(0, 5))
        
        self.path_entry = tk.Entry(input_frame, font=("Arial", 12), width=45, bg="white", fg="black", relief=tk.SUNKEN, bd=2)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        # Poga "Izvēlēties mapi"
        self.browse_btn = tk.Button(
            input_frame, 
            text="📁 Izvēlēties", 
            command=self.browse_folder,
            width=12
        )
        self.browse_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        # Poga "Analizēt mapi"
        self.analyze_btn = tk.Button(
            input_frame, 
            text="⚡ Analizēt mapi", 
            command=self.analyze_folder,
            bg="#4CAF50", 
            fg="white",
            font=("Arial", 12, "bold"),
            width=15
        )
        self.analyze_btn.pack(side=tk.LEFT)
        
        # Rezultātu lauks (ar ritjoslu)
        result_frame = tk.Frame(main_frame)
        result_frame.pack(fill=tk.BOTH, expand=True)
        
        self.result_text = scrolledtext.ScrolledText(
            result_frame, 
            wrap=tk.WORD, 
            font=("Courier", 16),
            height=20,
            bg="black",
            fg="lime",
            relief=tk.SUNKEN,
            bd=2,
            padx=10,
            pady=10
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # Sākotnējais teksts
        self.result_text.insert(tk.END, "Ievadiet mapes ceļu un nospiediet 'Analizēt mapi'")
        self.result_text.config(state=tk.DISABLED)
        
        # Statusa josla
        self.status_label = tk.Label(
            main_frame, 
            text="Gatavs", 
            bd=1, 
            relief=tk.SUNKEN, 
            anchor=tk.W,
            font=("Arial", 9)
        )
        self.status_label.pack(fill=tk.X, pady=(10, 0))
    
    def browse_folder(self):
        """Atver dialoglodziņu mapes izvēlei."""
        folder_path = filedialog.askdirectory(title="Izvēlieties mapi analīzei")
        if folder_path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder_path)
            self.status_label.config(text=f"Izvēlēta mape: {folder_path}")
    
    def analyze_folder(self):
        """Analizē norādīto mapi un parāda rezultātus."""
        directory = self.path_entry.get().strip()
        
        if not directory:
            messagebox.showwarning("Brīdinājums", "Lūdzu, ievadiet mapes ceļu!")
            return
        
        # Atjauno statusu
        self.status_label.config(text=f"Analizē mapi: {directory}...")
        self.root.update()
        
        # Analizē mapi (izmanto esošās funkcijas)
        result = get_folder_stats(directory)
        
        # Formatē un parāda rezultātus
        output = format_results(result, directory)
        
        # Ievieto rezultātus teksta laukā
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, output)
        self.result_text.config(state=tk.DISABLED)
        
        # Atjauno statusu
        if result is None:
            self.status_label.config(text=f"Kļūda: Mape '{directory}' nav atrasta!")
        else:
            self.status_label.config(text=f"Analīze pabeigta: {directory}")
    
    def run(self):
        """Palaid Tkinter galveno ciklu."""
        self.root.mainloop()


if __name__ == "__main__":
    # Palaid Tkinter programmu
    app = ProjektAnalizators()
    app.run()