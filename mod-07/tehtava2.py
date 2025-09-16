nimet = []
nimi = input("Syötä nimi, enter lopettaa: ")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
        nimi = input("Syötä nimi, enter lopettaa: ")
    else:
        print("Uusi nimi")
        nimet.append(nimi)
        nimi = input("Syötä nimi, enter lopettaa: ")
for n in nimet:
    print(n)