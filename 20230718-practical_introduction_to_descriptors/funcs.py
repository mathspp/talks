def get_name(self):
    return self.first + " " + self.last


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    get_name = get_name


john = Person("John", "Smith")
print(john.get_name())
print(get_name(john))
