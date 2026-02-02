data = {
    "juha": {
        "tyyppi": "opettaja",
        "osaaminen": "olematon",
        "arvosanat": [1,2,3,1,2,2],
        "uniikit_arvosanat": {1,2,3,1,2,2}
    },
    "marko": {
        "tyyppi": "ihminen",
        "osaaminen": "erinomainen",
        "arvosanat": [5,5,4,5,3],
        "uniikit_arvosanat": {5, 5, 4, 5, 3}
    }
}

print(data)

print(data["juha"]["arvosanat"])
print(data["juha"]["arvosanat"][-1])
print(data["juha"]["arvosanat"][0])

print("\nViimeisimmät arvosanat jokaisella henkilöllä data -sanakirjassa")
for avain in data:
    print(data[avain]["arvosanat"][-1])

if "olematon-avain" in data:
    print(data['olematon-avain'])

if "kissa" not in data:
    data['kissa'] = "best"

for avain in data:
    if "arvosanat" in data[avain]:
        print(data[avain]["arvosanat"][-1])

if 1 in data:
    print(data[1])


print(data)