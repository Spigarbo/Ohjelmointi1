lentoasemat = {}

jatketaan = True
while jatketaan:
    vastaus = int(input(f"Syötä 1. Jos halaut syöttää uuden lentoaseman, 2. jos haluat hakea jo syötetyn aseman tiedot, vai 3. jos haluat lopettaa: "))
    if vastaus == 1:
        ICAO = input("Syötä uuden kentän ICAO koodi: ")
        kentan_nimi = input("Syötä lentokentän nimi: ")
        lentoasemat[ICAO] = kentan_nimi
    elif vastaus == 2:
        ICAO_haku = input("Syötä haetun kentän ICAO koodi: ")
        print(lentoasemat[ICAO_haku])
    else:
        print("Lopetetaan")
        jatketaan = False
