import configparser
import os
import platform

from config.firefox import prefs
from utils.env import dotfile_path

try:
    root = dotfile_path('.mozilla/firefox')
    if platform.system() == 'Darwin':
        root = dotfile_path('Library/Application Support/Firefox')

    installs = os.path.join(root, 'installs.ini')
    _installs_cfg = configparser.ConfigParser()
    _installs_cfg.read(installs)

    default = os.path.join(root, _installs_cfg[_installs_cfg.sections()[0]]['Default'])

    def run():
        prefs.run()
except Exception:
    print('Error: need to setup firefox')

    def run():
        pass
