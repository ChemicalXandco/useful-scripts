import os

from config.helix import common
from utils.config import ConfigEditor


def run():
    with ConfigEditor(os.path.join(common.root, 'config.toml')) as cfg_edit:
        under = '[editor]'
        cfg_edit.add('idle-timeout = 0', under=under)


if __name__ == '__main__':
    run()
