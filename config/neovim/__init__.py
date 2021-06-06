import os

from config.neovim import init
from utils.env import dotfile_path, is_exe, do_nothing

root = dotfile_path('.config/nvim')

def _run():
    init.run()

if is_exe('nvim'):
    run = _run
else:
    run = do_nothing
