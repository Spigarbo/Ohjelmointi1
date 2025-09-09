import random
def heita(tahkot):
    luku = random.randint (1,int(tahkot))
    print(luku)
    return luku
tahkot = int(input("Kuinka monta tahkoa nopassa on? "))
luku = heita(tahkot)
while luku != tahkot:
    luku = heita(tahkot)