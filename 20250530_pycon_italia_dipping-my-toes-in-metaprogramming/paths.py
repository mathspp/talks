_OS = "Windows"

class Path:
    def __new__(cls, *args, **kwargs):
        if cls is Path:
            cls = WindowsPath if _OS == "Windows" else PosixPath
        return super().__new__(cls)

class PosixPath(Path):
    def __new__(cls, value):
        if _OS == "Windows":
            raise ValueError("Go home, you're drunk 🍻")

class WindowsPath(Path):
    def __new__(cls, value):
        if _OS != "Windows":
            raise ValueError("Go home, you're drunk 🍻")


_OS = "Linux"
print(Path("."))