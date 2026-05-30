import my_lib.terminal_utils
my_lib.terminal_utils.clear_screen()
"""
Uzdevums
Izveido klasi Students.
Katram studentam jābūt:
 vārdam
 vecumam
 kursam
Programmai jāpaprasa lietotājam ievadīt šos datus.
Pēc tam jāizveido objekts un jāizvada informācija par studentu.
Sagaidāmais rezultāts
 Ievadi vārdu: Anna
 Ievadi vecumu: 21
 Ievadi kursu: Python pamati
 Students: Anna
 Vecums: 21
 Kurss: Python pamati
"""
class Students:
    def __init__(self, vards, vecums, kurss):
        self.vards = vards
        self.vecums = vecums
        self.kurss = kurss
    def paradit(self):
        print(f"\nStudents: {self.vards}")
        print(f"Vecums: {self.vecums}")
        print(f"Kurss: {self.kurss}\n")


studenti = []

while True:
    print("\n--- Jauna studenta ievade ---")
    vards = input("Ievadi vārdu (vai 'n' lai beigtu): ")
    if vards.lower() == "n":
        break
    vecums = int(input("Ievadi vecumu: "))
    kurss = input("Ievadi kursu: ")
    
    studenti.append(Students(vards, vecums, kurss))

print("\n--- Visi studenti ---")
for students in studenti:
    students.paradit()
