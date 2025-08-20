leiviska_maara = input("Kuinka monta leiviskää? ")
naula_maara = input("Kuinka monta naulaa? ")
luoti_maara = input("Kuinka monta luotia? ")

luoti_massa = float(luoti_maara) * 13.3
naula_massa = float(naula_maara) * 13.3 * 32
leiviska_massa = float(leiviska_maara) * 13.3 * 32 * 20

yhteinen_massa = luoti_massa + naula_massa + leiviska_massa
kilot = float(yhteinen_massa) // 1000
grammat = float(yhteinen_massa) - float(kilot) * 1000

print(f"Yhteensä {kilot:.1f} kilogrammaa ja {grammat:.2f} grammaa")