# indeksit  0       1      2     3
# lopusta  -4      -3     -2     -1
nimet = ["Juha", "Matti", 123, "Viivi"]

print(nimet)
print(nimet[1])
print(nimet[0])
print(nimet[-1])
print(nimet[3])
print(nimet[-2])
print(nimet[-3])
print(nimet[-4])

if len(nimet) > 4:
    print(nimet[4])

print(nimet)
print("Nimet alkiosta 1 alkioon 3")
print(nimet[1:3])
print(nimet[:3])
print(nimet[3:])

uusi_lista = nimet[1:3]

print("Uuden listan tulostus")

print(uusi_lista)
print(nimet)

print(len(nimet))
print(len(uusi_lista))
print(len([]))
print(len([1,2,3]))
