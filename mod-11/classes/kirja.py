from .julkaisu import Julkaisu

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjailija, sivumaara):
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}")
        print(f" Kirjailija: {self.kirjailija}")
        print(f" Kirjan sivumäärä: {self.sivumaara}")