import shutil

def is_exe(name: str) -> bool:
    """Check whether `name` is on PATH and marked as executable."""
    detected = shutil.which(name) is not None
    if detected:
        print(f'Detected {name}')
    return detected

def do_nothing():
    pass
