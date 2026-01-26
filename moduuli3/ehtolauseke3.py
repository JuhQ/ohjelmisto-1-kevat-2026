#nimi = input("Anna nimi: ")
nimi = input("Anna nimi: ").lower()

print(nimi)
print(nimi.upper())

print(nimi)

if nimi == "Juha" or nimi == "juha" or nimi == "jUha":
    print("Syötteeksi annettiin Juha")

if nimi.lower() == "juha":
    print("Toinen if-lauseke: Syötteeksi annettiin Juha")


if "iffit on selviä":
    print("Otetaan läsnäolo")
