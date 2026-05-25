"""
Uzdevums
Izveido vārdnīcu:
serveris
Lauki:
nosaukums
ip
Mēģini nolasīt:
temperatura
izmantojot get()
"""

serveris = {
    "nosaukums": "Serveris1",
    "ip": "192.168.1.1"
}

# print(serveris["temperatura"])
print(serveris.get("temperatura", "\nTemperatura nav norādīta\n"))
