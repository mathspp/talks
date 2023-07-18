class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def name(self):
        return f"{self.first} {self.last}"

    @name.setter
    def name(self, new_name):
        first, last = new_name.split()
        self.first = first
        self.last = last


john = Person("John", "Smith")
john.first = "Rodrigo"
print(john.name)
