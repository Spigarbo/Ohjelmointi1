kuhan_mitta = float(input("Syötä kuhan pituus: "))
ali_jaama = 37 - float(kuhan_mitta)
if kuhan_mitta < 37:
    print(f"Kuha on alimittainen, pituudesta puuttuu {ali_jaama} cm.")
elif kuhan_mitta >= 37:
    print("Kuha on täysimittainen!")