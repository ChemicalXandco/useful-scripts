import pathlib
import shutil

def dotfile_path(fname: str) -> str:
    """Get the full path of a dotfile in the ~/ directory."""
    return str(pathlib.Path(f'~/{fname}').expanduser())

def is_exe(name: str) -> bool:
    """Check whether `name` is on PATH and marked as executable."""
    detected = shutil.which(name) is not None
    if detected:
        print(f'Detected {name}')
    return detected

def do_nothing():
    pass
