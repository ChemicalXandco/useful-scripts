from common import Exe

# ordered descending
editors = {
    'hx': Exe('hx'),  # helix
    'helix': Exe('helix'),  # some distrobutions such as arch linux rename hx to helix
    'kak': Exe('kak'),  # kakoune
    'nvim': Exe('nvim', '-i', 'NONE'),  # neovim
    'vim': Exe('vim'),
    'emacs': Exe('emacs'),
    'vi': Exe('vi'),
    'nano': Exe('nano'),
}
