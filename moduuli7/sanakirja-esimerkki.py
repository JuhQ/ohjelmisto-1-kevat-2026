nimet = {
    "juha": "040-12345678",
    "matti": "040-1234567",
    "1": "arvo",
    "0": "nolla-arvo"
}

print(nimet)
print(nimet["juha"])
print(nimet["matti"])
print(nimet["0"])
print(nimet["1"])

for avain in nimet:
    print(avain)
    print("Numero: " + nimet[avain])

print("\n\n")
print(nimet["juha"])

nimet["juha"] = "salainen numero"
print(nimet["juha"])

# tämä lisää uuden arvon, mikäli poliisi -avainta ei sanakirjassa jo ole
nimet["poliisi"] = "112"

# mikäli avain löytyy, sama operaatio yliajaa (muokkaa) aikaisempaa arvoa
nimet["poliisi"] = "118"

print(nimet)


for arvo in nimet:
    print(arvo + " = " + nimet[arvo])
    print(arvo,"=", nimet[arvo])
    print(f"{arvo} = {nimet[arvo]}")