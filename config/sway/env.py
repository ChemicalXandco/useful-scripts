import os

from config import sway
from utils.config import ConfigEditor
from utils.env import is_exe


def run():
    """
    Enviroment variables for the session
    """
    with ConfigEditor(os.path.join(sway.root, 'env')) as cfg_edit:
        if is_exe('firefox'):
            cfg_edit.add('MOZ_DBUS_REMOTE=1')
            cfg_edit.add('MOZ_ENABLE_WAYLAND=1')


if __name__ == '__main__':
    run()
