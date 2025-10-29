from classes.hissi import Hissi
def main():
    x = Hissi(1, 5)
    x.siirry_kerrokseen(int(input("Mihin kerrokseen haluat mennä? ")))
    print(x.kerros)
    print("Siirrytään alimpaan!")
    x.siirry_alimpaan()

main()