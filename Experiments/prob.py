import os
import subprocess

if os.name == 'nt':
    subprocess.run(['cls'], shell=True)
    subprocess.run(['cls'], shell=True)
else:
    subprocess.run(['clear'], shell=True)
    subprocess.run(['clear'], shell=True)

