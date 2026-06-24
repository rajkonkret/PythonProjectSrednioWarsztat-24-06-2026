# funkcja zagnieżdzona, wewnętrzna

fh = open('test.txt', "w")
fh.write("Zapisane\n")
fh.close()


# funkcja plik()
# zapis(), odczyt()

def plik(arg):
    print("Sprawdzam dysk...")

    def zapis():
        print("Zapisałem dane do pliku...")

    def odczyt():
        return "Odczytane dane z pliku..."

    if arg.casefold() == "zapis":

        return zapis  # zwraca adres funkcji
    else:
        return odczyt


odczyt_pliku = plik("odczyt")
print(odczyt_pliku)  # <function plik.<locals>.odczyt at 0x0000021B2A77CBF0>
print(type(odczyt_pliku))

print(odczyt_pliku())  # Odczytane dane z pliku...

zapis_pliku = plik("zapis")
zapis_pliku()  # Zapisałem dane do pliku...
