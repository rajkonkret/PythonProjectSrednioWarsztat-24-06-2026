# search()

class ContactList(list['Contact']):

    def search(self, name):
        matching_contacts = []

        for c in self:
            if name.casefold().strip() in c.name.casefold().strip():
                matching_contacts.append(c)

        return matching_contacts


cl = ContactList()
cl.append("Radek")
print(cl)  # ['Radek']


# cl.search("")


class Contact:
    """
    Klasa Contact
    """
    # all_contacts = []  # wspolna dla obiektów tej klasy
    all_contacts = ContactList()  # wspolna dla obiektów tej klasy
    x = 'TEST'

    def __init__(self, name, email):
        """

        :param name:
        :param email:
        """
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f"{self.name} {self.email}"


c1 = Contact("Radek", "raddek@wp.pl")
c2 = Contact("Tomek", "Tomek@wp.pl")
c3 = Contact("MArek", "MArek@wp.pl")
c4 = Contact("Zenek", "Zenek@wp.pl")

print(c1.all_contacts)
# [Radek raddek@wp.pl, Tomek Tomek@wp.pl, MArek MArek@wp.pl, Zenek Zenek@wp.pl]
print(Contact.all_contacts)
# [Radek raddek@wp.pl, Tomek Tomek@wp.pl, MArek MArek@wp.pl, Zenek Zenek@wp.pl]
# Contact.all_contacts.append("Red")

print(c1.x)  # TEST
print(c2.x)  # TEST
print(Contact.x)  # TEST

c2.x = "TEST2"
print(c1.x)  # TEST
print(c2.x)  # TEST2
print(Contact.x)  # TEST

c2.a = "Radek"
print(c2.a)  # Radek


# __slots__


class Suplier(Contact):
    """
    Klasa dziedziczy po kalsie Contact
    """

    def order(self, order):
        print(f"{order} zamówione od {self.name}")


sup1 = Suplier("Marek", "marek@wp.pl")
print(sup1)  # Marek marek@wp.pl
print(sup1.all_contacts)

sup1.order("kawa")  # kawa zamówione od Marek

print(50 * "-")
osoba = Contact.all_contacts.search("Radek")
for i in osoba:
    print(i)
    print(i.name)
    print(i.email)
# --------------------------------------------------
# Radek raddek@wp.pl
# Radek
# raddek@wp.pl
# _print
# print_,


class Friend(Suplier):
    """
    Klasa dziedziczy po Suplier
    """

    def __init__(self, name, email, phone="000000000"):
        pass