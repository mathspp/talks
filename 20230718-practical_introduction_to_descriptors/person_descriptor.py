import datetime as dt

class NameDescriptor:
    def __get__(self, person, cls):
        print(person, cls)
        return f"{person.first} {person.last}"


class AgeDescriptor:
    def __get__(self, person, cls):
        return dt.date.today().year - person.birthyear

class Person:
    age = AgeDescriptor()
    name = NameDescriptor()

    def __init__(self, first, last, birthyear):
        self.first = first
        self.last = last
        self.birthyear = birthyear


john = Person("John", "Smith", 1997)
print(john.name)
print(john.age)
