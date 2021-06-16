from config import bash, firefox, neovim, python
from utils.env import is_root

if is_root():
    raise RuntimeError('Do not run as root')

bash.run()
firefox.run()
neovim.run()
python.run()
