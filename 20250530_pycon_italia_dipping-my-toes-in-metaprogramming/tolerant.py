class TolerantFloat(float):
    def __new__(self, value, rel_tol):
        return super().__new__(cls, value)

    def __init__(self, value, rel_tol):
        self.rel_tol = rel_tol


TolerantFloat(3.14)