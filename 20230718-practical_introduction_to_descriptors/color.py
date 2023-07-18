class RGBComponent:
    def __init__(self, ...):
        ...

    def __get__(self, ...):
        ...


class Color:
    r = RGBComponent(...)
    g = RGBComponent(...)
    b = RGBComponent(...)

    def __init__(self, hex):
        self.hex = hex
