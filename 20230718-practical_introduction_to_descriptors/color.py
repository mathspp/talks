class RGBComponent:
    def __init__(self, idx):
        self.idx = idx

    def __get__(self, color, cls):
        hex = color.hex
        values = hex[1 + 2 * self.idx:2 * self.idx + 3]
        return int(values, 16)


class Color:
    r = RGBComponent(0)
    g = RGBComponent(1)
    b = RGBComponent(2)
    hello = "Hello"

    def __init__(self, hex):
        self.hex = hex

clr = Color("#ff0000")  # ~ (ff, 00, 00)
print(clr.r)
