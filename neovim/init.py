import os

import neovim
from utils.config import ConfigEditor

def run():
    with ConfigEditor(os.path.join(neovim.root, 'init.vim'), '" ') as cfg_edit:
        cfg_edit.add('set tabstop=4', under='" length of an actual \\t character:')
        cfg_edit.add('set softtabstop=-1', under='" length to use when editing text (eg. TAB and BS keys)\n" (0 for ‘tabstop’, -1 for ‘shiftwidth’):')
        cfg_edit.add('set shiftwidth=0', under='" length to use when shifting text (eg. <<, >> and == commands)\n" (0 for ‘tabstop’):')
        cfg_edit.add('set shiftround', under='" round indentation to multiples of ‘shiftwidth‘ when shifting text\n" (so that it behaves like Ctrl-D / Ctrl-T):')

        cfg_edit.add('set expandtab', under='" if set, only insert spaces; otherwise insert \\t and complete with spaces:')

        cfg_edit.add('set autoindent', under='" reproduce the indentation of the previous line:')
        cfg_edit.add('set smartindent', under='" try to be smart (increase the indenting level after ‘{’, decrease it after ‘}’, and so on):')
        cfg_edit.add('filetype plugin indent on', under='" use language‐specific plugins for indenting (better):')

if __name__ == '__main__':
    run()
