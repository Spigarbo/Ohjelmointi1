käyttäjätunnus = "python"
salasana = "rules"
yritykset = 0
print("Syötä käyttäjätunnus ja salasana.")
yritys1 = input("Käyttäjätunnus: ")
yritys2 = input("Salasana: ")
while yritys1 != käyttäjätunnus or yritys2 != salasana:
    yritykset = yritykset + 1
    if yritykset < 5:
        print("Väärä käyttäjätunnus tai salasana, yritä uudelleen!")
        yritys1 = input("Käyttäjätunnus: ")
        yritys2 = input("Salasana: ")
    else:
        print("Pääsy evätty")
        break
else:
    print("Tervetuloa!")

