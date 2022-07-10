from common import Exe

# ordered descending
editors = [
    Exe('hx'),  # helix
    Exe('helix'),  # some distrobutions such as arch linux rename hx to helix
    Exe('kak'),  # kakoune
    Exe('nvim', '-i', 'NONE'),  # neovim
    Exe('vim'),
    Exe('emacs'),
    Exe('vi'),
    Exe('nano')
]
