class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def get_name(self):
        return f"{self.first} {self.last}"


john = Person("John", "Smith")
john.first = "Rodrigo"
print(john.get_name())
