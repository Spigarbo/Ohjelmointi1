from random import randint
from classes.romuauto import RomuAuto
from classes.Kilpailu import Kilpailu

osallistujat = []
for i in range(1,11):
    osallistujat.append(RomuAuto(f"ABC-" + str(i), randint(100,200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, osallistujat)


while not kilpailu.kilpailu_ohi():
    for auto in osallistujat:
        auto.kiihdytä(randint(-10, 15))
    kilpailu.tunti_kuluu()
    if kilpailu.ajettu % 10 == 0:
        kilpailu.tulosta_tilanne()
