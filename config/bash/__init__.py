from config.bash import alternative, arguments, history, prompt, python
from utils.env import dotfile_path, is_exe, do_nothing

bashrc = dotfile_path('.bashrc')

def _run():
    alternative.run()
    arguments.run()
    history.run()
    prompt.run()
    python.run()

if is_exe('bash'):
    run = _run
else:
    run = do_nothing
