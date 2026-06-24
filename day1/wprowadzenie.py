# https://peps.python.org/pep-0008/
# snake_case
import sys

print("")
print('')

# blake
print("pierwsza linia")
print('pierwsza linia')

# ctrl / - komentarz
# print("pierwsza linia')
#   File "C:\Users\CSComarch\PycharmProjects\PythonProject\day1\wprowadzenie.py", line 11
#     print("pierwsza linia')
#           ^
# SyntaxError: unterminated string literal (detected at line 11)
#
# Process finished with exit code 1

"""
komentarz
    wielolinijkowy (dokumentacja)"""

info = """
tekst
wielolinijkowy
    zachowuje
        formatowanie"""

print(info)
# "tekst
# wielolinijkowy
#     zachowuje
#         formatowanie"

# typowanie dynamiczne
print(type(info))  # <class 'str'>

# ctrl alt l - formatowanie
info = 90
print(type(info))  # <class 'int'> liczba całkowita

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

info = "Radek"
print(info)

print("12" + "45")  # konkatenacja -> 1245
print(12 * "40")  # 404040404040404040404040

# print("12" + 40)  # TypeError: can only concatenate str (not "int") to str
# silne typowanie - nie zmienia sam typów
# rzutowanie
print(int(12) + int("40"))  # 52

# float - liczba zmiennoprzecinkowa
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308,
# min=2.2250738585072014e-308, min_exp=-1021,
# min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# błąd zaokrąglenia
print(0.1 + 0.9)  # 1.0
print(0.1 + 0.2)  # 0.30000000000000004
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

# decimal() - pozwala ominąć problem błędu zaokrąglenia

# boolean
# True, False
# 1, 0

print(bool(100))  # True
print(bool("radek"))  # True

print(bool(""))  # False
print(bool("0"))  # True
