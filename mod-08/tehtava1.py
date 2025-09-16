import mysql.connector


yhteys = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'miio',
    password= 'salasana',
    autocommit=True
)

ICAO = input("Syötä lentokentän ICAO koodi: ")
def haeLentokentta(koodi):
    sql = f"SELECT * FROM airport WHERE ident=%s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchone()
    return tulos

kentta = (haeLentokentta(ICAO))
print(kentta['name'], kentta['municipality'])