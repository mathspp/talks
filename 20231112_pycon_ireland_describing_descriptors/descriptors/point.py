class ReadOnly:
    def __get__(self, point, cls):
        return getattr(point, f"_{self.attr_name}")

    def __set__(self, point, name):
        raise RuntimeError("stooopid 🤡")

    def __set_name__(self, cls, name):
        print(f"set name w/ {name = }")
        self.attr_name = name


class Point:
    x = ReadOnly()
    y = ReadOnly()

    def __init__(self, x, y):
        self._x = x
        self._y = y


p = Point(1, 2)
# p.x = 73
print(p.x)
print(p.y)
