class Person:
    def __init__(self, *names):
        self.names = list(names)

    @property
    def first(self):
        return self.names[0]

    # @first.setter
    # def first(self, name):
    #     self.names[0] = name


steve = Person("Steve", "Holden")
steve.first = "Rodrigo"
print(steve.first)
