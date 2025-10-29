luku = int(input("Syötä jokin kokonaisluku: "))

if luku < 1:
    print("Luku on liian pieni")
else:
    for i in range(luku+1):
        if i%2 == 0:
            print(1)
