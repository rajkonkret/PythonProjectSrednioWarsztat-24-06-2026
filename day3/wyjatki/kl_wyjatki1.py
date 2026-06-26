# print(2 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonProject\day3\wyjatki\kl_wyjatki1.py", line 1, in <module>
#     print(2 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1

# raise ZeroDivisionError
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonProject\day3\wyjatki\kl_wyjatki1.py", line 10, in <module>
#     raise ZeroDivisionError
# ZeroDivisionError
#
# Process finished with exit code 1

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę cąlkowitą większą od zera: "))
    if x <= 0:
        raise MyException("Liczba musi być większa od zera")
except MyException as e:
    print("Wartośc musi być większa od zera", e)
except ValueError as e:
    print("Błąd wartości:", e)
except Exception as e:
    print("Bład:", e)
else:  # tylko gdy nie ma błedu
    print("Działanie na x:", x * 2)
finally: # wykona się zawsze
    print("Koniec")
