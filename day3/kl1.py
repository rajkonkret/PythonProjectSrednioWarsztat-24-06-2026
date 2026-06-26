# klasy - element programowania obiektowego
# szablon, przepis
# obiekt (instancja)
# metod (funkcje)
# cechy (zmienne)
# metody inicjalizująca __init__ - konstruktor
# hermetyzacja, dziedziczenie, polimorfizm, abstrakacja
import math
from os import name


# PascalCase, UpperCamelCase
class MyFirstClass:
    """
    Klasa w Pythonie
    """

    def __init__(self, x=0, y=0):
        """
        Metoda inicjalizująca - konstruktor
        :param x:
        :param y:
        """
        # self.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: int, y: int) -> None:
        """
        Ustawia nowe x i y
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        """
        For a two dimensional point (x, y), this is equivalent to computing the hypotenuse
         of a right triangle using the Pythagorean theorem, sqrt(x*x + y*y).
        :param other:
        :return:
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    # metoda opisowa - bezpośredni print(), str()
    def __str__(self):
        return f"{self.x, self.y}"

    # reprezentacja obiektu dla programisty
    def __repr__(self):
        return f"{self.__class__.__name__} {self.x, self.y}"


ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x000002644A4D97F0>
# po dodaniu __str__ -> (0, 0)
print(MyFirstClass.__doc__)  # Klasa w Pythonie
# pydoc -b
# pydoc -w .\kl1.py
print(ob.x)  # 0
print(ob.y)  # 0
print(ob)  # (0, 0)

point1 = MyFirstClass(5, 9)
print(point1)  # (5, 9)

point1.move(8, 90)
print(point1)  # (8, 90)

# reset()
point1.reset()
print(point1)  # (0, 0)

# calculate() odległość euklidesowa
point2 = MyFirstClass(90, 76)

print(point1.calculate(point2))
# 117.79643458101778

point3 = MyFirstClass(87, 12)
point4 = MyFirstClass(43, 233)

print(point3)
print(point4)
# (87, 12)
# (43, 233)

lista = [point1, point2, point3, point4]

print(lista)
# po dopisaniu __repr__
# [MyFirstClass (0, 0),
# MyFirstClass (90, 76),
# MyFirstClass (87, 12),
# MyFirstClass (43, 233)]
