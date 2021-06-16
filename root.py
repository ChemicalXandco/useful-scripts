from config import pacman
from utils.env import is_root

if not is_root():
    raise RuntimeError('Need to run as root')

pacman.run()
