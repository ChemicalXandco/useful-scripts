import os
import shutil

from config import sway
from utils.config import ConfigEditor
from utils.env import is_exe


def exec_cmd(bind, cmd):
    return f'bindsym {bind} exec {cmd}'


def run():
    config_path = os.path.join(sway.root, 'config')
    if not os.path.isfile(config_path):
        shutil.copy('/etc/sway/config', config_path)

    with ConfigEditor(config_path, '#') as cfg_edit:
        under = '# Your preferred terminal emulator'
        var = '$term'
        if is_exe('alacritty'):
            cfg_edit.add(f'set {var} alacritty', under=under, start=True)
        elif is_exe('kitty'):
            cfg_edit.add(f'set {var} kitty', under=under, start=True)
        cfg_edit.add(
                exec_cmd('$mod+Return', var),
                under='# Start a terminal',
                )

        under = ('# Your preferred application launcher\n'
                 '# Note: pass the final command to swaymsg so that the result'
                 'ing window can be opened\n'
                 '# on the original workspace that the command was run on.')
        var = '$menu'
        if is_exe('wofi'):
            cfg_edit.add(f'set {var} wofi --show run', under=under, start=True)
        cfg_edit.add(
                exec_cmd('$mod+d', var),
                under='# Start your launcher',
                )

        under = 'bar {'
        cfg_edit.remove('    position top')
        cfg_edit.add('    position bottom', under=under)

        cfg_edit.add('default_border none')
        cfg_edit.add('include /etc/sway/config.d/*')


if __name__ == '__main__':
    run()
