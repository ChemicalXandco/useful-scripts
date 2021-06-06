import itertools
import functools
import re
import subprocess


@functools.total_ordering
class Version:
    def __init__(self, *version: tuple[int], delimiter: str='.'):
        self.version = version
        self.delimiter = delimiter

    def init_str(self, version: str):
        self.version = tuple([ int(i) for i in version.split(self.delimiter) ])
        return self

    def __repr__(self):
        return f"Version(*{self.version}, delimiter='{self.delimiter}')"

    def __str__(self):
        return self.delimiter.join([ str(i) for i in self.version ])

    def __eq__(self, other):
        for i, j in itertools.zip_longest(self.version, other.version, fillvalue=0):
            if i != j:
                return False
        return True
    def __lt__(self, other):
        for i, j in itertools.zip_longest(self.version, other.version, fillvalue=0):
            if i < j:
                return True
        return False
    # other ordering operations are generated using functools.total_ordering


def get_version(command: str, arguments: list[str]=['--version']) -> Version:
    res = subprocess.check_output([command]+arguments)
    output = res.decode('utf-8')
    match = re.search(r'(?:\d+(\D))+\d+', output)
    return Version(delimiter=match.group(1)).init_str(match.group(0))
