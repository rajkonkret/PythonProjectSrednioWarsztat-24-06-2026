class Contact:
    """
    Klasa Contact
    """
    all_contacts = []  # wspolna dla obiektów tej klasy
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
