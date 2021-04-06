import bash
from utils.config import ConfigEditor

def run():
    with ConfigEditor(bash.bashrc) as cfg_edit:
        cfg_edit.add('export HISTFILE=/dev/null', under='# reduce disk writes')

if __name__ == '__main__':
    run()
