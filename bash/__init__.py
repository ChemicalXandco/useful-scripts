from pathlib import Path

from bash import alternative, history, prompt, python
from utils.env import is_exe, do_nothing

bashrc = str(Path('~/.bashrc').expanduser())

def _run():
    alternative.run()
    history.run()
    prompt.run()
    python.run()

if is_exe('bash'):
    run = _run
else:
    run = do_nothing
