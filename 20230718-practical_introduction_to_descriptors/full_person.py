class NameDescriptor:
    def __init__(self, idx):
        self.idx

    def __get__(self, person, cls):
        return person.name.split()[self.idx]

class FullNamePerson:
    first = NameDescriptor(0)
    middle = NameDescriptor(slice(1, -1))
    last = NameDescriptor(-1)

    def __init__(self, name):
        self.name = name
