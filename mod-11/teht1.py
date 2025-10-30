from classes.lehti import Lehti
from classes.kirja import Kirja

julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(Kirja("Harry Potter", "J.K. Rowling", 1000))


for t in julkaisut:
    t.tulosta_tiedot()
