from config.bash import (
        alias, alternative, arguments, git, history, prompt, python,
        )
from utils.env import dotfile_path, is_exe

bashrc = dotfile_path('.bashrc')


def run():
    alias.run()
    alternative.run()
    arguments.run()
    if is_exe('git'):
        git.run()
    history.run()
    prompt.run()
    python.run()
