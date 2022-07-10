import os
from typing import Optional
import urllib.request

from utils.env import is_exe, run


class ExecutableNotFoundError(OSError):
    pass


class Exe:
    """
    An executable file accessible on $PATH
    """

    def __init__(self, name: str, *args: tuple[str, ...]):
        self.name = name
        self.args = list(args)

    def _can_run(func):
        def inner(self, *args, **kwargs):
            if not self.exists:
                raise ExecutableNotFoundError()

            return func(self, *args, **kwargs)

        return inner

    @property
    @_can_run
    def command(self) -> str:
        return ' '.join([self.name] + self.args)

    @property
    def exists(self) -> bool:
        return is_exe(self.name)

    @_can_run
    def run(self, *args: tuple[str, ...]) -> str:
        run(self.name, *self.args, *args)


class File:
    """
    A file that exists on the filesystem
    """

    def __init__(self, path: str):
        self._path = path

    @property
    def exists(self) -> bool:
        return os.path.isfile(self._path)

    @property
    def path(self) -> str:
        if not self.exists:
            raise FileNotFoundError(f'{self._path} does not exist')

        return self._path

    @property
    def name(self) -> str:
        return os.path.basename(self.path)


class Url:
    """
    A remote resource that can be downloaded
    """

    def __init__(self, url: str, name: Optional[str] = None):
        self.url = url

        if not name:
            name = os.path.basename(url)
        self.name = name

    def download(self, directory: str) -> File:
        if not os.path.isdir(directory):
            os.mkdir(directory)

        path = os.path.join(directory, self.name)
        if os.path.exists(path):
            print(f'{path} already exists, skipping download')
        else:
            print(f'downloading {self.url} to {path}')
            urllib.request.urlretrieve(url=self.url, filename=path)

        return File(path)
