# dekorator - funkcja, która przyjmuje inną funkcję jako argument
# upiksza, dodaje, modyfikuje działanie
# wykorzystuje mechanizm funkcji wew

def dekor(funk):
    def wew():
        print("Dekorator. Dodatkowy wynik")
        return funk()

    return wew  # zwracamy adres funkcji


@dekor
def nasza_funkcja():
    print("Funkcja, którą chcemy udekorować")


nasza_funkcja()
# Dekorator. Dodatkowy wynik
# Funkcja, którą chcemy udekorować