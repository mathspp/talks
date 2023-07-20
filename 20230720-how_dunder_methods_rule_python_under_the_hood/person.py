class Person:
    def __init__(self, first, last):
        print("I'm in init")
        self.first = first
        self.last = last

    def __repr__(self):
        return f"Person({self.first}, {self.last})"

    def __str__(self):
        return self.first


john = Person("John", "Smith")
print(john)
my_list = [john]
print(my_list)
