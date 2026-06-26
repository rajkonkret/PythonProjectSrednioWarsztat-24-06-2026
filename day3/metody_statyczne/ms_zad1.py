# metoda statyczna - nie potrzebuje obiektu klasy

class Matematyka:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


# kalk = Matematyka()
# print(kalk.dodaj(56, 90))  # 146

print(Matematyka.dodaj(5, 90))
print(Matematyka.dodaj(90, 78))  # 168
