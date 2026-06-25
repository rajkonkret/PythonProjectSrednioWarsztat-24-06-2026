# zrobic dekorator
# zamiana na małe litery, oczyszczenie z białych znaków
# wypisac wynik działania funkcji kolorem czerwonym i bold

def lower_decorator(funk):
    def wew(*args, **kwargs):
        # *args - dowolna ilość argumentów po pozycji 1,2,3,4
        # **kwargs - argumenty słownikowe a=10, b=20
        return funk(*args, **kwargs).lower().strip()

    return wew  # zwracamy adres funkcji


@lower_decorator
def nasza_funkcja(a, b, c):
    print(a, b, c)
    return "Hello world"


print(nasza_funkcja(1, 2, c=90))
