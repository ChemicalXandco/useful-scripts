from config import bash
from utils.config import ConfigEditor
from utils.env import is_exe


def run():
    with ConfigEditor(bash.bashrc) as cfg_edit:
        under = '# power'
        cfg_edit.add("alias s='sudo shutdown now'", under=under)

        under = '# fetch updates'
        cmds = []
        # Arch
        if is_exe('paru'):
            cmds.append('paru')
        elif is_exe('pacman'):
            cmds.append('pacman -Syu')

        if is_exe('flatpak'):
            cmds.append('flatpak update')

        cmds.sort()
        strcmds = ' && '.join(cmds)
        cfg_edit.add(f"alias u='{strcmds}'", under=under)

        under = '# launch desktop'
        if is_exe('sway'):
            cfg_edit.add(
                "exec systemctl --wait --user start sway.service",
                under=under,
                )


if __name__ == '__main__':
    run()
