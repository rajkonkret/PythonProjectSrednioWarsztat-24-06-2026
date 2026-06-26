# Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM)
# – sposób odwzorowania obiektowej architektury systemu informatycznego na bazę danych (lub inny element systemu)
# o relacyjnym charakterze.

# orm w pythonie -> peewe, sqlalchemy
# pip install sqlalchemy

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# echo=True - podgląd logów bazy danych
engine = create_engine('sqlite:///moja_baza_pytanie.db', echo=True)
Base = declarative_base()


# CREATE TABLE person (
# 	id INTEGER NOT NULL,
# 	name VARCHAR,
# 	age VARCHAR,
# 	PRIMARY KEY (id)
# )

# model, encja - klasa odwzorowująca tabele w bazie danych
class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)

    def __repr__(self):
        return f"{self.name}"


# tworzenie tabel
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(name="Radek", age="23")
session.add(person)
session.commit()
# INSERT INTO person (name, age) VALUES (?, ?) ('Radek', '23')

persons = session.query(Person).all()
print(persons)
# SELECT person.id AS person_id, person.name AS person_name, person.age AS person_age
# FROM person

for p in persons:
    print(p.name)
    print(p.id)
# Radek
# 1
# Radek
# 2
# Radek
# 3
# Radek
# 4

# pgAdmin, dbeaver, Toad, sqldeveloper
# tablePlus, Heidi
# DbBrowser for sqlite
