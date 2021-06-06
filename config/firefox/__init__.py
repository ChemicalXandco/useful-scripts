import configparser
import os

from config.firefox import prefs
from utils.env import dotfile_path, is_exe, do_nothing

def _run():
    prefs.run()

if is_exe('firefox'):
    root = dotfile_path('.mozilla/firefox')

    installs = os.path.join(root, 'installs.ini')
    _installs_cfg = configparser.ConfigParser()
    _installs_cfg.read(installs)

    default = os.path.join(root, _installs_cfg[_installs_cfg.sections()[0]]['Default'])

    run = _run
else:
    run = do_nothing
