from classes.auto import Auto

autot = []

auto1 = Auto("ABC-123", 142)
auto2 = Auto("YGJ-633", 205)
auto3 = Auto("ZHU-326", 210)

autot.append(auto1)
autot.append(auto2)
autot.append(auto3)

for auto in autot:
    print(f"""
    Rekisteritunnus: {auto.rekisteritunnus}
    Huippunopeus: {auto.huippunopeus}
    Nopeus: {auto.nopeus}
    Matka: {auto.matka}
    """)
