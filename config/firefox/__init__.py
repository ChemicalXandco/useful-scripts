import configparser
import os

from config.firefox import prefs
from utils.env import dotfile_path

root = dotfile_path('.mozilla/firefox')

installs = os.path.join(root, 'installs.ini')
_installs_cfg = configparser.ConfigParser()
_installs_cfg.read(installs)

default = os.path.join(root, _installs_cfg[_installs_cfg.sections()[0]]['Default'])

def run():
    prefs.run()
