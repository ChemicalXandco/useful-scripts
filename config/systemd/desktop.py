from utils.config import ConfigEditor
from utils.env import is_exe


def sway():
    with ConfigEditor('/etc/systemd/user/sway.service') as cfg_edit:
        under = '[Unit]'
        cfg_edit.add('After=graphical-session-pre.target', under=under)
        cfg_edit.add('Wants=graphical-session-pre.target', under=under)
        cfg_edit.add('BindsTo=graphical-session.target', under=under)
        cfg_edit.add('Documentation=man:sway(5)', under=under)
        cfg_edit.add('Description=sway', under=under)

        under = '[Service]'
        cfg_edit.add('TimeoutStopSec=10', under=under)
        cfg_edit.add('RestartSec=1', under=under)
        cfg_edit.add('Restart=on-failure', under=under)
        cfg_edit.add('ExecStart=dbus-run-session sway', under=under)
        cfg_edit.add('EnvironmentFile=-%h/.config/sway/env', under=under)
        cfg_edit.add('Type=simple', under=under)


def run():
    if is_exe('sway'):
        sway()


if __name__ == '__main__':
    run()
