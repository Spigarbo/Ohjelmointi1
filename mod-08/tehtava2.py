import mysql.connector


yhteys = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'miio',
    password= 'salasana',
    autocommit=True
)


def haeLentokentta(koodi):
    sql = f"SELECT type, COUNT(*) FROM airport WHERE iso_country=%s GROUP BY type"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchall()
    return tulos
maakoodi = input("Syötä maakoodi: ")
kentat = (haeLentokentta(maakoodi))

for kentta in kentat:
    print(kentta)
