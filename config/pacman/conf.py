from utils.config import ConfigEditor

def run():
    with ConfigEditor('/etc/pacman.conf', '# ') as cfg_edit:
        # Progress bar easter egg
        cfg_edit.add('ILoveCandy', under='[options]')

if __name__ == '__main__':
    run()
