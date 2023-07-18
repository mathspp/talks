from time import sleep

from git.repo import Repo

PATH = "../.git"
COMMIT = "Auto push."


def push():
    repo = Repo(PATH)
    repo.git.add(".")
    repo.index.commit(COMMIT)
    origin = repo.remote(name="origin")
    origin.push()


if __name__ == "__main__":
    while True:
        push()
        sleep(60)
