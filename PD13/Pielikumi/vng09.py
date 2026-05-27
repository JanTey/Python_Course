import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
try:
    vecums = int(input())
    print(100 / vecums)
except:
    print("Kaut kas nogāja greizi")
Uzlabo.
Nosacījums:
lietotājam jāsaprot problēma.
"""

while True:
    try:
        vecums = int(input("\nIevadi savu vecumu: "))
        print(f"\n100 / {vecums} = {100 / vecums:.2f}\n")
        break
    except ValueError:
        print("Kļūda: Lūdzu, ievadi veselu skaitli (ciparus)!")
    except ZeroDivisionError:
        print("Kļūda: Vecums nevar būt 0!")
