eläimet = {"Kissa", "Koira", "Kettu"}

# Indeksin perusteella ei voi hakea
#print(eläimet[0])

# katsotaan löytyykö haluttu arvo joukosta
if "Kissa" in eläimet:
    print("kissa löytyi")

print(eläimet)
print(eläimet)

eläimet.add("Alpakka")
eläimet.add("Alpakka")
eläimet.add("Alpakka")
eläimet.add("Alpakka")
eläimet.add("Alpakka")
eläimet.add("Alpakka")
eläimet.add("Alpakka")
eläimet.add("Alpakka")
eläimet.add("Alpakka")
eläimet.add("Alpakka")
eläimet.add("Alpakka")
eläimet.add("Alpakka")



print(eläimet)

for eläin in eläimet:
    print("Eläin: " + eläin)

tyhjä_lista = list()

# tyhjä joukko pitää luoda set() -funktiokutsulla, {} luo tyhjän sanakirjan
tyhjä_joukko = set()
print(tyhjä_lista)
print(tyhjä_joukko)

tyhjä_joukko.add("Arvo")

print(tyhjä_joukko)
