import os

from config.helix import common
from utils.config import ConfigEditor
from utils.ui import select

themes = [
    'default',
    'base16_default',
    'acme',
    'autumn_night',
    'autumn',
    'base16_default_dark',
    'base16_default_light',
    'base16_terminal',
    'bogster',
    'boo_berry',
    'catppuccin',
    'dark_plus',
    'dracula_at_night',
    'dracula',
    'everforest_dark',
    'everforest_light',
    'gruvbox_light',
    'gruvbox',
    'ingrid',
    'meliora',
    'monokai_pro_machine',
    'monokai_pro_octagon',
    'monokai_pro_ristretto',
    'monokai_pro_spectrum',
    'monokai_pro',
    'monokai',
    'night_owl',
    'noctis_bordo',
    'nord_light',
    'nord',
    'onedark',
    'onelight',
    'pop-dark',
    'rose_pine_dawn',
    'rose_pine',
    'serika-dark',
    'serika-light',
    'snazzy',
    'solarized_dark',
    'solarized_light',
    'spacebones_light',
    'tokyonight_storm',
    'tokyonight',
]


def run():
    with ConfigEditor(os.path.join(common.root, 'config.toml')) as cfg_edit:
        if not cfg_edit.exists('theme'):
            print('no theme set')
            print('select a theme for helix')
            theme = select(*themes, default=themes[0])
            cfg_edit.add(f'theme = "{theme}"', start=True)

        under = '[editor]'
        cfg_edit.add('idle-timeout = 0', under=under)


if __name__ == '__main__':
    run()
