import re
from typing import Callable, Optional

def read(func):
    """
    Read and then position at start.
    """
    def decorator(self, *args, **kwargs):
        if 'file_contents' in kwargs.keys(): # do not overwrite file_contents if provided
            raise KeyError('do not use file_contents argument; it is provided automatically')
        kwargs['file_contents'] = self._io.read()
        self._io.seek(0) # position at start
        result = func(self, *args, **kwargs)
        return result
    return decorator


class ConfigEditor():
    def __init__(self, cfg_file: str, comment_str: str = '#'):
        self._cfg_file = cfg_file
        self._comment_str = comment_str.strip()

    def __enter__(self):
        print('Opening', self._cfg_file)
        self._io = open(self._cfg_file, 'r+')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._io.close()
        print(self._cfg_file, 'successfully edited')

    @read
    def add_line(self, content: str, under: Optional[str] = None, file_contents=''):
        """
        Add a line to a config file.
        The line will be added under a heading if under is set.
        If the heading does not exist it will be created.
        Use \\n for multiple lines.
        Prints and ends if the desired content already exists in the file.
        If the desired content already exists in the file but is commented out it will be uncommented.

        Args:
            content: the line(s) to add
            under: the line to add the content under as a regex
        """
        if self._is_comment(content_start := file_contents.find(content)):
            self.uncomment(content_start)
            print('uncommented', content)
            return
        elif content_start != -1:
            print('line', content, 'already exists')
            return
        if under:
            if match := file_contents.find(under) != -1:
                insert_point = match + len(under) + 1
            else:
                print('could not find heading', under)
                heading = under + '\n'
                self._insert(heading, 0)
                insert_point = len(heading)
                print('made new heading:', under)
        else:
            insert_point = 0
        self._insert(content+'\n', insert_point)

    @read
    def for_each(self, regex: re.Pattern, function: Callable[[int], None], file_contents=''):
        """
        Run a function on all lines matching the regex.

        Supported functions:
            ConfigEditor.comment
            ConfigEditor.uncomment
        """
        offset = 0
        print('searching for', regex)
        for m in regex.finditer(file_contents):
            offset += function(m.start()+offset)
            print('successfully did operation on', m.group())

    @read
    def comment(self, content_start: int, file_contents='') -> int:
        """
        Comment out all lines matching the regex if they are not already commented out.
        """
        if not self._is_comment(content_start):
            self._insert(self._comment_str + ' ', content_start)
            return len(self._comment_str) + 1
        return 0

    @read
    def uncomment(self, content_start: int, file_contents='') -> int:
        """
        Uncomment all lines matching the regex if they are commented.
        """
        if self._is_comment(content_start):
            comment_start = self._comment_start(content_start)
            self._write(file_contents[:comment_start] + file_contents[content_start:])
            return len(self._comment_str) * -1
        return 0

    @read
    def _insert(self, text: str, index: int, file_contents=''):
        self._write(file_contents[:index] + text + file_contents[index:])

    def _write(self, text: str):
        self._io.write(text)
        self._io.truncate() # get rid of old text
        self._io.seek(0) # position at start

    @read
    def _is_comment(self, content_start: int, file_contents='') -> bool:
        start = self._comment_start(content_start)
        substr = file_contents[start:content_start]
        return substr.strip() == self._comment_str

    @read
    def _comment_start(self, content_start: int, file_contents='') -> int:
        line_start = file_contents.rfind('\n', 0, content_start)
        if line_start == -1:
            line_start = 0
        else:
            line_start += 1
        return line_start
