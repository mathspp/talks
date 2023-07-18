class RGBComponent:
    def __init__(self, idx):
        self.idx = idx

    def __get__(self, ...):
        ...


class Color:
    r = RGBComponent(0)
    g = RGBComponent(1)
    b = RGBComponent(2)
    hello = "Hello"

    def __init__(self, hex):
        self.hex = hex

clr = Color("#ff0000")  # ~ (ff, 00, 00)
print(clr.hello)
