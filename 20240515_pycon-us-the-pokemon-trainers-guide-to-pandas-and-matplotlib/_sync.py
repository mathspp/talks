from pathlib import Path
from time import sleep

from git import Repo


repo = Repo(Path(__file__).parent)

while True:
    repo.index.add("*")
    repo.index.commit("Auto sync commit")
    repo.remote().push()
    sleep(60)
