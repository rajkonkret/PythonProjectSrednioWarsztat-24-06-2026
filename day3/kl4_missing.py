# słownik
# gdy nie ma klucza: KeyError
# __missing__

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


d1 = DefaultDict()
print(type(d1))  # <class '__main__.DefaultDict'>
print(d1)  # {}
print(d1['name'])  # default

d2 = {}
# print(d2['name'])  # KeyError: 'name'
