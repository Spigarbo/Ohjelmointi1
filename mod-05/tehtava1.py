import random
summa = 0
silmaluvut = []
heittojen_maara = int(input("Syötä heitettävien noppien määrä: "))
while heittojen_maara > 0:
    silmaluvut.append(random.randint(1,6))
    heittojen_maara = heittojen_maara - 1
print(silmaluvut)
for heitot in silmaluvut:
    summa = summa + int()
print(f" Lukujen summa on {summa}")