import math

alkukorkeus = float(input("Anna esineen korkeus: "))

PUTOAMISKIIHTYVYYS = 9.81

kokonaisaika = math.sqrt(2 * alkukorkeus / PUTOAMISKIIHTYVYYS)

aika = 0
while aika < kokonaisaika:
    matka = 0.5 * PUTOAMISKIIHTYVYYS * aika ** 2
    print(f"Korkeus: {(alkukorkeus - matka):.2f}m")
    aika = aika + 1
print(f"kokonaisaika: {kokonaisaika:.2f}s")