from .romuauto import RomuAuto
import random

class Kilpailu:
    def __init__(self, nimi, pituus, autolista):
        self.nimi = "Suuri romuralli"
        self.pituus = pituus
        self.autot = autolista
        self.ajettu = 0

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kulje(1)
        self.ajettu += 1


    def nopeuden_muutos(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
            for auto in self.autot:
                print(auto.autontiedot())


    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
            return False

