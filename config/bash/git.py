from config import bash
from utils.config import ConfigEditor


def run():
    with ConfigEditor(bash.bashrc) as cfg_edit:
        under = '# git shortcuts'
        cfg_edit.add(
                "alias gita='git add . && git diff --cached'",
                under=under,
                )
        cfg_edit.add(
                ("alias gitc='read -p \"message: \" git_commit_message && g"
                    "it commit -m \"$git_commit_message\"'"),
                under=under,
                )


if __name__ == '__main__':
    run()
