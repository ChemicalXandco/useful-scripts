from pathlib import Path

from bash import history, python

bashrc = str(Path('~/.bashrc').expanduser())

def run():
    history.run()
    python.run()
