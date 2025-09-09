def vaihto(luku):
    vastaus = luku * 3.785
    return vastaus
luku = float(input("Syötä bensiinin määrä gallonina: "))
while luku >= 0:
    vastaus = vaihto(luku)
    print(vastaus)
    luku = float(input("Syötä bensiinin määrä gallonina: "))
