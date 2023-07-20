class NoneList:
    def __init__(self):
        self.values = {}

    def __getitem__(self, key):
        return self.values.get(key)

    def __setitem__(self, key, value):
        self.values[key] = value
