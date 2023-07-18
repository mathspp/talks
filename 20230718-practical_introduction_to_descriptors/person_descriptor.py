class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last


class NameDescriptor:
    def __get__(self, person, cls):
        return f"{person.first} {person.last}"
