import mysql.connector


yhteys = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'miio',
    password= 'salasana',
    autocommit=True
)

def haeLentokentat():
    sql = "SELECT * FROM airport"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def haeLentokentta(koodi):
    sql = f"SELECT * FROM airport WHERE ident=%s"
    print(sql)
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchone()
    return tulos


kentta = (haeLentokentta('EFHK'))
print(kentta['name'], kentta['type'])
# kentat = haeLentokentat()

# for kentta in kentat:
    #print(f"Nimi: {kentta['name']}, ICAO: {kentta['ident']}")