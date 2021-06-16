from config.pacman import conf
from utils.env import is_exe, do_nothing

def _run():
    conf.run()

if is_exe('pacman'):
    run = _run
else:
    run = do_nothing
