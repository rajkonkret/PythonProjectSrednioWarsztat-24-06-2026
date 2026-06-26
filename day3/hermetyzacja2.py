class Car:
    """Klasa opisująca samochód"""

    def __init__(self, model):
        self.__model = model

    @property
    def model(self):
        """
        getter
        :return:
        """
        print("Wypisuje model")
        return self.__model


car = Car("Renault")
print(car.model)
# Wypisuje model
# Renault
