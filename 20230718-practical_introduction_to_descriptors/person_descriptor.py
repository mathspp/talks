class NameDescriptor:
    def __get__(self, person, cls):
        print(person, cls)
        return f"{person.first} {person.last}"

class Person:
    name = NameDescriptor()

    def __init__(self, first, last):
        self.first = first
        self.last = last


john = Person("John", "Smith")
print(john.name)
print(Person.name)
