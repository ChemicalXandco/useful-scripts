from config.alacritty import alacritty_yml
from utils.env import cpu_name, dotfile_path

root = dotfile_path('.config/alacritty')

opengl_unsupported = [
    'P8400', 'P8600', 'P8700', 'P8800'  # ThinkPad X200
]


def _opengl_supported(cpu: str) -> bool:
    for unsupported in opengl_unsupported:
        if unsupported in cpu:
            return False
    return True


def command() -> str:
    cmd = ''

    cpu = cpu_name()
    if not _opengl_supported(cpu):
        print(f'unsupported opengl with cpu {cpu}; alacritty will use software rendering')
        cmd += 'export LIBGL_ALWAYS_SOFTWARE=1 && '

    cmd += 'alacritty'

    return cmd


def run():
    alacritty_yml.run()
