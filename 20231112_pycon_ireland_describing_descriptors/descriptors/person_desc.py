class FirstDesc:
    def __get__(self, person, cls):
        return person.names[0]

    def __set__(self, person, name):
        person.names[0] = name


class LastDesc:
    def __get__(self, person, cls):
        print(f"last get {person = }")
        return person.names[-1]

    def __set__(self, person, name):
        person.names[-1] = name


class NameDesc:
    def __init__(self, index_into_names):
        self.index_into_names = index_into_names

    def __get__(self, person, cls):
        print(f"last get {person = }")
        return person.names[self.index_into_names]

    def __set__(self, person, name):
        raise RuntimeError("stooopid 🤡")
        person.names[self.index_into_names] = name


class Person:
    # first = FirstDesc()
    # last = LastDesc()
    first = NameDesc(0)
    last = NameDesc(-1)

    def __init__(self, *names):
        self.names = list(names)


steve = Person("Steve", "Holden")
steve.first = "Rodrigo"
print(steve.first)
print(steve.last)
