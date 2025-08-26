tuumat = input("Anna tuuma määrä: ")

while int(tuumat) >= 0:
    print(f"{tuumat} tuumaa on {float(tuumat) * 2.54}cm")
    tuumat = input("Anna tuuma määrä: ")
else:
    print("Negatiivinen luku")