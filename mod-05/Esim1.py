numerot = []

numero = int(input("Anna ensimmäinen numero: "))
while numero >= 0 and numero !="":
    numerot.append(numero)
    numero = int(input("Anna seuraava numero: "))

numerot.sort()
print(numerot)
if 10 in numerot:
    print("luku 10 löytyi")
else:
    print("lukua 10 ei löytynyt")