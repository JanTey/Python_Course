import os
import subprocess

def clear_screen():
    """Notīra termināļa ekrānu"""
    if os.name == "nt":  # Windows
        subprocess.run(["cls"], shell=True)
        subprocess.run(["cls"], shell=True)
    else:  # Mac / Linux
        subprocess.run(["clear"], shell=True)
        subprocess.run(["clear"], shell=True)
