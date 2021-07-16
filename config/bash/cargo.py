from config import bash
from utils.config import ConfigEditor


def run():
    with ConfigEditor(bash.bashrc) as cfg_edit:
        under = '# cargo (rust) shortcuts'
        cfg_edit.add("alias rs='cargo build && cargo run'", under=under)


if __name__ == '__main__':
    run()
