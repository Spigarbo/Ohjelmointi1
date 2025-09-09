def summa(numerot):
    vastaus = sum(numerot)
    return vastaus
numerot = []
luku = input("Syötä jokin kokonaisluku, enter lopettaa: ")
while luku != "":
    numerot.append(int(luku))
    luku = input("Syötä jokin kokonaisluku, enter lopettaa: ")
vastaus = summa(numerot)
print(vastaus)