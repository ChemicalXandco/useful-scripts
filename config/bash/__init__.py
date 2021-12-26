from config.bash import (
        alias, alternative, arguments, git, history, profile, prompt, python,
        )
from utils.env import dotfile_path, is_exe

profile_path = dotfile_path('.bash_profile')
bashrc = dotfile_path('.bashrc')


def run():
    alias.run()
    alternative.run()
    arguments.run()
    if is_exe('git'):
        git.run()
    history.run()
    profile.run()
    prompt.run()
    python.run()
