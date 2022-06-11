from utils.env import is_exe, is_root

if not is_root():
    raise RuntimeError('Need to run as root')

import packages
if packages.package_manager.root:
    packages.run()

if is_exe('makepkg'):
    from config import makepkg
    makepkg.run()
if is_exe('pacman'):
    from config import pacman
    pacman.run()
