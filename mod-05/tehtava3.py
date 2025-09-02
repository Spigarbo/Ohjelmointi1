luku = int(input("Syötä jokin kokonaisluku: "))
if luku < 2:
    print("Luku ei ole alkuluku")
else:
    for i in range(2,luku):
        if luku % i == 0:
            print("Luku ei ole alkuluku")
            break
    else:
        print("Luku on alkuluku")