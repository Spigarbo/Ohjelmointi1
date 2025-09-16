import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'miio',
    password= 'salasana',
    autocommit=True
)

def haeLentokentta(koodi):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchone()
    return tulos

maakoodi1 = input("Syötä maakoodi: ")
kentat1 = (haeLentokentta(maakoodi1))
maakoodi2 = input("Syötä toinen maakoodi: ")
kentat2 = (haeLentokentta(maakoodi2))

koordinaatit1 = kentat1['latitude_deg'], kentat1['longitude_deg']
koordinaatit2 = kentat2['latitude_deg'], kentat2['longitude_deg']

print(distance.distance(koordinaatit1, koordinaatit2).km)
