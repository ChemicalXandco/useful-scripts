from config import git
from utils.config import ConfigEditor
from utils.ui import get_editor


def run():
    with ConfigEditor(git.gitconfig_path) as cfg_edit:
        under = '[core]'
        cfg_edit.add(f'    editor = {get_editor()}', under=under)

        # https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases
        under = '[alias]'
        cfg_edit.add('    unstage = reset HEAD --', under=under)
        # add all
        cfg_edit.add('    al = !git add . && git diff --cached', under=under)
        # commit with message
        cfg_edit.add('    cm = commit -m', under=under)


if __name__ == '__main__':
    run()
