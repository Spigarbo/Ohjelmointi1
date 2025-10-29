from random import randint

from classes.auto import Auto

def jatketaanko():
    jatketaan = True
    for auto in autot:
        if auto.matka>=10000:
            jatketaan = False
    return jatketaan

def nopeuden_muutos():
    for auto in autot:
        auto.kiihdytä(randint(-10,15))
        auto.kulje(1)


def lopputiedot():
    for auto in autot:
        print(auto.autontiedot())

autot = []
for i in range(1,11):
    autot.append(Auto(f"ABC-" + str(i), randint(100,200)))

while jatketaanko() == True:
    nopeuden_muutos()
lopputiedot()




