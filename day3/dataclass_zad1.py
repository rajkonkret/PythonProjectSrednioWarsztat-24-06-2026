# class Person:
#     def __init__(self, fn, ln, id):
#         self.fn = fn
#         self.ln = ln
#         self.id = id
#
#
# p1 = Person("JAn", "Kowalski", 1)
# print(p1) # <__main__.Person object at 0x00000122604797F0>

from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    lat_name: str
    id: int

    def greets(self):
        print("My name is:", self.first_name)


p1 = Person("Jan", 'Kowalski', 1)
print(p1)  # Person(first_name='Jan', lat_name='Kowalski', id=1)

p2 = Person("Anna", 'Krawiec', 2)
print(p2)  # Person(first_name='Anna', lat_name='Krawiec', id=2)

people = [p1, p2]
print(people)
# [Person(first_name='Jan', lat_name='Kowalski', id=1), Person(first_name='Anna', lat_name='Krawiec', id=2)]
