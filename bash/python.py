import bash
from utils.config import ConfigEditor

def run():
    with ConfigEditor(bash.bashrc) as cfg_edit:
        cfg_edit.add_line("alias python='export PYTHONPATH=$PWD && python'", under='# python env')
        cfg_edit.add_line("alias pytest='export PYTHONPATH=$PWD && pytest'", under='# python env')

if __name__ == '__main__':
    run()
