ekaluku = input("Syötä jokin luku: ")
while ekaluku != "":
    tokaluku = input("Syötä seuraava luku: ")
    if tokaluku == "":
        print(f"Suurin lukusi oli {maksimi}, ja pienin lukusi {minimi}")
        break
    else:
        maksimi = tokaluku
        minimi = ekaluku
        vikaluku = input("Syötä seuraava luku: ")
        if int(vikaluku) > int(maksimi):
            maksimi = vikaluku
        if int(vikaluku) < int(minimi):
            minimi = vikaluku
        if vikaluku == "":
            print(f"Suurin lukusi oli {maksimi}, ja pienin lukusi {minimi}")
            break
else:
    print("Et syöttänyt lukua")
