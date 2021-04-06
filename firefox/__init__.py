from configparser import ConfigParser
from pathlib import Path
import os

from firefox import prefs

root = Path('~/.mozilla/firefox').expanduser()

installs = os.path.join(root, 'installs.ini')
_installs_cfg = ConfigParser()
_installs_cfg.read(installs)

default = os.path.join(root, _installs_cfg[_installs_cfg.sections()[0]]['Default'])

def run():
    prefs.run()
