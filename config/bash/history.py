from config import bash
from utils.config import ConfigEditor
from utils.env import dotfile_path, rm

def run():
    with ConfigEditor(bash.bashrc) as cfg_edit:
        cfg_edit.add('export HISTFILE=/dev/null', under='# reduce disk writes')

        rm(dotfile_path('.bash_history'))

if __name__ == '__main__':
    run()
