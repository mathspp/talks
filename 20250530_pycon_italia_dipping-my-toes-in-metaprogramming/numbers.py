class Number:
    def __new__(cls, value):
        print(cls)
        if cls is Number:
            cls = OddNumber if value % 2 else EvenNumber
        return super().__new__(cls)

class EvenNumber(Number):
    def __new__(cls, value):
        if value % 2:
            raise ValueError("Go home, you're drunk 🍻")

class OddNumber(Number): ...

print(EvenNumber(3))