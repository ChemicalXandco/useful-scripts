from pathlib import Path

from bash import history, prompt, python

bashrc = str(Path('~/.bashrc').expanduser())

def run():
    history.run()
    prompt.run()
    python.run()
