from pathlib import Path
import os

from neovim import init
from utils.env import is_exe, do_nothing

root = Path('~/.config/nvim').expanduser()

def _run():
    init.run()

if is_exe('nvim'):
    run = _run
else:
    run = do_nothing
