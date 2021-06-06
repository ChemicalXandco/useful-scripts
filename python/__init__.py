from pathlib import Path

from python import history
from utils.env import is_exe, do_nothing

pythonrc = str(Path('~/.pythonrc').expanduser())

def _run():
    history.run()

if is_exe('python') or is_exe('python3'):
    run = _run
else:
    run = do_nothing
