
ika = float(input("Anna ikä: "))
"""
monen rivin kommentti
print(int(ika))
print(float(ika))

ika = float(ika)
"""

if ika >= 65:
    print("Olet eläkeiässä.")
elif ika >= 18:
    print("Olet työiässä.")
elif ika >= 7:
    print("Olet koululainen.")
else:
    print("Olet pikkulapsi.")

print("Suoritus jatkuu pääohjelmassa")