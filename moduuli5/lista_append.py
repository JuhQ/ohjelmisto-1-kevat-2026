nimet = []

nimi = input("Anna nimi: ")

while nimi != "":
    nimet.append(nimi)
    print(len(nimet))

    nimi = input("Anna nimi: ")

print(nimet)

if "Juha" in nimet:
    print("Jee")

"""
for loopin selitys
nimi = nimet[0]
nimi = nimet[1]
nimi = nimet[2]
"""

for nimi in nimet:
    print(f"Nimi: {nimi}")