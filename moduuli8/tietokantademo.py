import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='password',
    autocommit=True,
    # mysql.connector.errors.DatabaseError: 1273 (HY000): Unknown collation: 'utf8mb4_0900_ai_ci'
    # if you see above error, fix could be to define collation as shown below:
    collation='utf8mb3_general_ci'
)

def hae_data():
    sql = "SELECT id, name, municipality FROM airport WHERE id >= 100000 ORDER BY id LIMIT 5"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)

    tulos = kursori.fetchall()

    print(tulos)
    print(tulos[0])
    print(tulos[0][0])

    for rivi in tulos:
        print(rivi)

        (name, id, city) = rivi

        print(f"NAME = {name}")
        print(f"ID = {id}")

        #id = rivi[0]
        #print(f"NAME = {name}")
        #print(f"ID = {id}")

        for alkio in rivi:
            print(f"  {alkio}")


def lisää_uusi_kenttä(ident, name, id):
    sql = f"INSERT INTO airport (ident, name, id) VALUES ('{ident}', '{name}', {id})"

    kursori = yhteys.cursor()
    kursori.execute(sql)

    print(kursori.rowcount)

hae_data()

# kommenteissa koska sama id ei voi esiintyä monta kertaa
# lisää_uusi_kenttä("1234", "Karamalmin pienlentokonekenttä", 100000)


