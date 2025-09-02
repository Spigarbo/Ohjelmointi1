lukujono = []
numero = input("Syötä jokin luku, enter sulkee ")
while numero != "":
    lukujono.append(int(numero))
    numero = input("Syötä uusi luku, enter sulkee ")
lukujono.sort(reverse=True)
for numerot in lukujono[:5]:
    print(numerot)
