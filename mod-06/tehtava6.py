import math
def vertailija(koko, hinta):
    nelio = (math.pi * (float(koko) / 2) ** 2) / 10000
    hinta = int(hinta)
    if hinta == 0:
        return 0
    yksikkohinta = nelio / hinta
    return yksikkohinta

koko = input("Syötä ensimmäisen pizzan halkaisija: ")
hinta = input("Syötä ensimmäisen pizzan hinta euroina: ")

yksikkohinta1 = vertailija(koko, hinta)

koko = input("Syötä toisen pizzan halkaisija: ")
hinta = input("Syötä toisen pizzan hinta euroina: ")

yksikkohinta2 = vertailija(koko, hinta)

if yksikkohinta1 > yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikkohinta1 < yksikkohinta2:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Vastine rahalle on yhtä hyvä.")
