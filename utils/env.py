import os
import pathlib
import platform
import shutil
import subprocess


def run(*args: list[str]) -> str:
    res = subprocess.check_output(args)
    return res.decode('utf-8')


def rm(path: str) -> bool:
    """
    Remove the file at `path`

    Args:
        path: path of the file to remove
    Returns:
        bool: if the file existed
    """
    if (exists := os.path.isfile(path)):
        os.remove(path)
        print(f'Removed {path}')
    return exists


def dotfile_path(fname: str) -> str:
    """Get the full path of a dotfile in the ~/ directory."""
    return str(pathlib.Path(f'~/{fname}').expanduser())


def is_exe(name: str) -> bool:
    """Check whether `name` is on PATH and marked as executable."""
    detected = shutil.which(name) is not None
    if not detected and platform.system() == 'Darwin':
        try:
            run('open', '-n', '-a', name, '--args', '--version')
            detected = True
        except subprocess.CalledProcessError:
            pass
    if detected:
        print(f'Detected {name}')
    return detected


def is_root() -> bool:
    return os.geteuid() == 0


def select_font(*fonts: list[str], default: str) -> str:
    """
    Select a font from fonts passed as arguements.
    Select first available font with fallback to `default`.
    """
    available_fonts = run('fc-list')
    for font in fonts:
        if font in available_fonts:
            return font
    return default
