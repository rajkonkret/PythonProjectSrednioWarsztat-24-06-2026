# klasy - element programowania obiektowego
# szablon, przepis
# obiekt (instancja)
# metod (funkcje)
# cechy (zmienne)
# metody inicjalizująca __init__ - konstruktor
# hermetyzacja, dziedziczenie, polimorfizm, abstrakacja

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

    # metoda opisowa
    def __str__(self):
        return f"{self.x, self.y}"


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
