nimet = ("Juha", "Matti")

print(nimet[0])
print(nimet[1])
print(nimet[-1])

nimet2 = ("Ei-juha", nimet[1])

#nimet[0] = "Ei-juha"

print(nimet2[0])

print(len(nimet))

hedelmat = "banaani", "omena", "tomaatti"
(eka, toka, kolmas) = hedelmat
eka = hedelmat[0]
toka = hedelmat[1]
kolmas = hedelmat[2]

print(hedelmat)
print(nimet)

print(hedelmat[0])

print(kolmas)

monikko = ("Kissa", "Koira", "Kettu", "Kojootti")
(kissa, koira, kettu, _) = monikko

print(kettu)

monikkojen_monikko = ((1,2,3), (1,), ("Kissa", "Kettu"), "merkkijono", ["kettu"], [1,2,3,4, (1, [234, 233,4])])
print(monikkojen_monikko)

print(monikkojen_monikko[2])
print(monikkojen_monikko[2][1])
print(monikkojen_monikko[-1])
print(monikkojen_monikko[-1][-1])
print(monikkojen_monikko[-1][-1][-1])
viimeinen_monikko = monikkojen_monikko[-1][-1]
print(monikkojen_monikko[-1][-1][-1][-2])
#print(monikkojen_monikko[4][4][1][1])

print(viimeinen_monikko)
print(viimeinen_monikko[-1][-2])

for arvo in monikkojen_monikko:
    print("Monikon iterointi")
    print(arvo)