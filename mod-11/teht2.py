from classes.uusiauto import Auto
from classes.sahkoauto import Sahkoauto
from classes.polttomoottoriauto import Polttomoottoriauto

autot = []

auto1 = Sahkoauto("ABC-15", 180, 52.5)
auto2 = Polttomoottoriauto("ACD-123", 165, 32.3)

autot.append(auto1)
autot.append(auto2)

auto1.kiihdytä(120)
auto2.kiihdytä(115)

auto1.kulje(3)
auto2.kulje(3)

for auto in autot:
    print(Auto.autontiedot(auto))