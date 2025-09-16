vuodenajat = {(12 , 1 , 2) : "Talvi",
              (3, 4, 5) : "Kevat",
              (6, 7, 8) : "Kesa",
              (9, 10, 11) : "Syksy"}

valinta = int(input("Kirjoita kuukauden numero, ohjelma kertoo mihin vuodenaikaan se kuuluu: "))
for kuukaudet, vuodenaika in vuodenajat.items():
    if valinta in kuukaudet:
        print(f"Kuukauden numero {valinta} vuodenaika on {vuodenaika}.")