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

# słownik, który gdy nie ma klucza tworzy taki klucz z wartością domyslna
class AutoDict(dict):
    def __missing__(self, key):
        # slownik['name'] = 'Radek'
        self[key] = 0
        return key


a1 = AutoDict()
print(a1)  # {}
print(a1['name'])
print(a1)
# {'name': 0}
