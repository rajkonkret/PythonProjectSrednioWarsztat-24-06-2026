# longest_key()

class LongestKeyDict(dict):

    def longest_key(self):
        return max(self.keys(), key=len, default=None)


art = LongestKeyDict()
art['name'] = 'Radek'
art['age'] = 12
art['active'] = True

print(art.longest_key())  # active
