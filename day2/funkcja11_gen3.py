dane = [x for x in range(5)]
print(dane)
print(type(dane))
# [0, 1, 2, 3, 4]
# <class 'list'>

# wyrażenie generatorowe
dane = (x for x in range(5))
print(dane)
print(type(dane))  # <class 'generator'>
# [0, 1, 2, 3, 4]

print(next(dane))
print(next(dane))
print(next(dane))
print(next(dane))

print(45 * "-")
lista = [1, 2, 3, 4, 5]
lista_iter = iter(lista)
print(next(lista_iter))
# ---------------------------------------------
# 1
