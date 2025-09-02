import random
from selectors import SelectSelector

luku = random.randint(1,10)
arvaus = int(input("Arvaa luku 1 ja 10 väliltä: "))
while int(arvaus) != int(luku):
    if arvaus < luku:
        print("Liian pieni!")
        arvaus = int(input("Arvaa luku 1 ja 10 väliltä: "))
    elif arvaus > luku:
        print("Liian suuri!")
        arvaus = int(input("Arvaa luku 1 ja 10 väliltä: "))
else:
    print("Oikein meni")