from config.alacritty import alacritty_yml
from utils.env import dotfile_path

root = dotfile_path('.config/alacritty')


def run():
    alacritty_yml.run()
