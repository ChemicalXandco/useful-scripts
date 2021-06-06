from python import history
from utils.env import dotfile_path, is_exe, do_nothing

pythonrc = dotfile_path('.pythonrc')

def _run():
    history.run()

if is_exe('python') or is_exe('python3'):
    run = _run
else:
    run = do_nothing
