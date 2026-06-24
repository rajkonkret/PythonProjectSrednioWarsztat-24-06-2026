# funkcja - fragment kodu, który mozna wywołąc wielokrotnie
from typing import Tuple

print()


# deklaracja funkcji
def odejmij():
    print(10 - 4)


odejmij()  # 6


def odejmij(a, b, c):
    print(a - b - c)


# odejmij() # TypeError: odejmij() missing 3 required positional arguments: 'a', 'b', and 'c'
odejmij(1, 2, 3)  # -4


# duck typing
# argumenty z wartościami domyślnymi
def dodaj(a=0, b=0, c=0):
    print(a + b + c)


dodaj()
dodaj(1, 2)
dodaj(1, 2, 3)
# 0
# 3
# 6

# po nazwie
dodaj(c=9, b=98)  # 107

# mieszane
dodaj(10, 2, c=90)  # 102


# dodaj(b=90, c=87, 3) # SyntaxError: positional argument follows keyword argument

# print(dodaj(4) + dodaj(5))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

# funkcje zwracajace wynik
def mnozenie(a, b):
    return a * b  # zwraca wynik


print(mnozenie(5, 7))  # 35

print(mnozenie(5, 6) + mnozenie(7, 89))  # 653


# funkcja zwracająca więcej niż jedną wartość
def mnozenie2(a, b):
    return a, b, a * b  # (7 ,9, 63)


print(mnozenie2(5, 6))  # (5, 6, 30)
print(mnozenie2("a", 9))  # ('a', 9, 'aaaaaaaaa')

# rozpakowanie krotki
a, b, wynik = mnozenie2(7, 9)
print(f"{a} * {b} = {wynik}")  # 7 * 9 = 63


# podpowiedzi typów
def mnozenie3(a: int, b: int) -> Tuple[int, int, int]:
    return a, b, a * b


a, b, wynik = mnozenie3("a", 9)
print(f"{a} * {b} = {wynik}")  # a * 9 = aaaaaaaaa
