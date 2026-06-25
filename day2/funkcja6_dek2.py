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

# https://en.wikipedia.org/wiki/ANSI_escape_code
print("\033[31mHello\033[0m")  # kolorki

# pip install colorama
from colorama import Fore, Style, init

init(autoreset=True)


def czerwony_bold(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)

        # print(
        #     Style.BRIGHT + Fore.RED + str(wynik) + Style.RESET_ALL
        # )
        # return wynik
        return Style.BRIGHT + Fore.RED + str(wynik) + Style.RESET_ALL

    return wrapper


@czerwony_bold
def komunikat():
    return "Uwaga! Wystąpił bład."


print(komunikat())
# Uwaga! Wystąpił bład.
# Uwaga! Wystąpił bład.
