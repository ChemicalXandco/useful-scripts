from shutil import which

def is_exe(name):
    """Check whether `name` is on PATH and marked as executable."""
    return which(name) is not None

def do_nothing():
    pass
