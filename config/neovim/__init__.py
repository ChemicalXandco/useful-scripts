from config.neovim import init
from utils.env import dotfile_path

root = dotfile_path('.config/nvim')

def run():
    init.run()
