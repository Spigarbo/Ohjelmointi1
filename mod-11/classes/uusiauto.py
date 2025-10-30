import random

class Auto:
    def __init__(self, new_rekisteritunnus, new_huippunopeus):
        self.rekisteritunnus = new_rekisteritunnus
        self.huippunopeus = new_huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, new_nopeus):
        self.nopeus = self.nopeus + new_nopeus
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += tunnit * self.nopeus


    def autontiedot(self):
        return (f"""
        Autosi tiedot:
        Rekisteritunnus: {self.rekisteritunnus}
        Huippunopeus: {self.huippunopeus}
        Nopeus: {self.nopeus}
        Matka: {self.matka}
        """)