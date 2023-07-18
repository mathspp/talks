class NameDescriptor:
    def __init__(self, idx):
        self.idx = idx

    def __get__(self, person, cls):
        return person.name.split()[self.idx]

    def __set__(self, person, new_name):
        names = person.name.split()
        names[self.idx] = new_name
        person.name = " ".join(names)

class FullNamePerson:
    first = NameDescriptor(0)
    middle = NameDescriptor(slice(1, -1))
    last = NameDescriptor(-1)

    def __init__(self, name):
        self.name = name
