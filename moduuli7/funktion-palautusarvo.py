import random

def heitä():
    eka, toka = random.randint(1, 6), random.randint(1, 6)
    return eka, toka

def heita2():
    (eka, toka) = (random.randint(1, 6), random.randint(1, 6))
    return (eka, toka)

def heitä3():
    return (random.randint(1, 6), random.randint(1, 6))

def heitä4():
    return random.randint(1, 6), random.randint(1, 6)

noppa1, noppa2 = heitä()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

noppa1, noppa2 = heita2()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

noppa1, noppa2 = heitä3()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

noppa1, noppa2 = heitä4()
print(f"Nopista tuli {noppa1} ja {noppa2}.")