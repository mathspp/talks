class RGBComponent:
    def __init__(self, ...):
        ...

    def __get__(self, ...):
        ...


class Color:
    r = RGBComponent(...)
    g = RGBComponent(...)
    b = RGBComponent(...)
    hello = "Hello"

    def __init__(self, hex):
        self.hex = hex

clr = Color("#ff0000")
print(clr.hello)
