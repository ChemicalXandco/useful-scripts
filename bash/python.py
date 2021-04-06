import bash
from utils.config import ConfigEditor
from utils.env import is_exe

def run():
    with ConfigEditor(bash.bashrc) as cfg_edit:
        cfg_edit.add("alias pytest='export PYTHONPATH=$PWD && pytest'", under='# python env')

        if is_exe('python3') and not is_exe('python'):
            cfg_edit.add("alias python='export PYTHONPATH=$PWD && python3'", under='# python env')
        else:
            cfg_edit.add("alias python='export PYTHONPATH=$PWD && python'", under='# python env')

if __name__ == '__main__':
    run()
