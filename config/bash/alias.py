from config import bash
from utils.config import ConfigEditor
from utils.env import is_exe


def run():
    with ConfigEditor(bash.bashrc) as cfg_edit:
        under = '# fetch updates'
        cmds = []

        # Arch
        if is_exe('paru'):
            cmds.append('paru')
        elif is_exe('pacman'):
            cmds.append('sudo pacman -Syu')

        # Debian
        if is_exe('apt'):
            cmds.append('sudo apt update')
            cmds.append('sudo apt upgrade')

        # Brew
        if is_exe('brew'):
            cmds.append('brew update')
            cmds.append('brew upgrade')

        if is_exe('flatpak'):
            cmds.append('flatpak update')

        cmds.sort()
        strcmds = ' && '.join(cmds)
        cfg_edit.add(f"alias u='{strcmds}'", under=under)


if __name__ == '__main__':
    run()
