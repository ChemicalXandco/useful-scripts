from config.bash import alternative, arguments, history, prompt, python
from utils.env import dotfile_path

bashrc = dotfile_path('.bashrc')

def run():
    alternative.run()
    arguments.run()
    history.run()
    prompt.run()
    python.run()
