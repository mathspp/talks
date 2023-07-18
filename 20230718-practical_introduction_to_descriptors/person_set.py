class NameDescriptor:
    def __get__(self, person, cls):
        print(person, cls)
        return f"{person.first} {person.last}"
    
    def __set__(self, person, new_name):
        first, last = new_name
        person.first = first
        person.last = last


class Person:
    name = NameDescriptor()

    def __init__(self, first, last):
        self.first = first
        self.last = last


john = Person("John", "Smith")
print(john.name)
