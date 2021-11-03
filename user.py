from utils.env import is_exe, is_root

if is_root():
    raise RuntimeError('Do not run as root')

if is_exe('alacritty'):
    from config import alacritty
    alacritty.run()
if is_exe('bash'):
    from config import bash
    bash.run()
if is_exe('firefox'):
    from config import firefox
    firefox.run()
if is_exe('mako'):
    from config import mako
    mako.run()
if is_exe('nvim'):
    from config import neovim
    neovim.run()
if is_exe('python') or is_exe('python3'):
    from config import python
    python.run()
if is_exe('sway'):
    from config import sway
    sway.run()
