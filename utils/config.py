import os
import re
from typing import Callable, Optional

def read(func):
    """
    Read and then position at start.
    """
    def decorator(self, *args, **kwargs):
        if 'file_contents' in kwargs.keys(): # do not overwrite file_contents if provided
            raise KeyError('do not use file_contents argument; it is provided automatically')
        kwargs['file_contents'] = self._read()
        result = func(self, *args, **kwargs)
        return result
    return decorator


class ConfigEditor():
    def __init__(self, cfg_file: str, comment_delimiter: str = '#'):
        self._cfg_file = cfg_file
        self._comment_delimiter = comment_delimiter.strip()

    def __enter__(self):
        if not os.path.isfile(self._cfg_file):
            print(self._cfg_file, 'does not exist, creating...')
            try:
                directory = os.path.dirname(self._cfg_file)
                os.mkdir(directory)
                print(directory, 'successfully created')
            except FileExistsError:
                pass
            open(self._cfg_file, 'w').close()

        print('Opening', self._cfg_file)
        self._io = open(self._cfg_file, 'r+')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._io.close()
        print(self._cfg_file, 'successfully edited')

    @read
    def add(self, content: str, under: Optional[str]='', start: Optional[bool]=False, replace_matching: str='=', file_contents=''):
        """
        Add a line.
        The line will be added under a heading if under is set.
        If the heading does not exist it will be created.
        Use \\n for multiple lines.
        Prints and ends if the desired content already exists in the file.
        If the desired content already exists in the file but is commented out it will be uncommented.

        Args:
            content: the line(s) to add
            under: the line to add the content under as a regex
            start: add the line to the start of the file if `under` is not found
            replace_matching: check if a similar statement to the content exists
        """
        if self._is_comment(content_start := file_contents.find(content)):
            self.uncomment(content_start)
            print(f'Uncommented " {content} "')
            return
        elif content_start != -1:
            return

        if replace_matching:
            matching_content = content[:content.find(replace_matching)+1]
            if matching_content and matching_content in file_contents:
                self.remove(matching_content)
                file_contents = self._read()

        if start:
            insert_point = 0
        else:
            insert_point = len(file_contents)

        if under:
            if (match := file_contents.find(under)) != -1:
                insert_point = match + len(under) + 1
            else:
                print('Could not find heading', under)
                heading = under + '\n'
                self._insert(heading, insert_point)
                insert_point += len(heading)
                print('Made new heading:', under)

        self._insert(content+'\n', insert_point)
        print(f'Added line " {content} "')

    @read
    def replace(self, content: str, with_this: str, file_contents=''):
        """
        Replace a line.
        Use \\n for multiple lines.
        Prints and ends if the line(s) to replace cannot be found.

        Args:
            content: the line(s) to replace
            with_this: the line to add the content under as a regex
        """
        if not content:
            print('Nothing to replace')
            return
        if not content in file_contents:
            print('Could not find the line(s) "', content, '" to replace')
            return
        content_start = self.remove(content)
        self._insert(with_this+'\n', content_start)
        print('Replaced line(s) "', content, '" with "', with_this, '"')

    @read
    def remove(self, content: str, file_contents='') -> int:
        """
        Remove the line that contains `content`
        """
        if (content_start := file_contents.find(content)) == -1:
            print(f'Could not find " {content} "')
            return -1
        if (content_end := file_contents.find('\n', content_start) + 1) == 0:
            content_end = len(file_contents)

        self._write(file_contents[:content_start] + file_contents[content_end:])
        print(f'Removed " {content} "')

        return content_start

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
        Comment out the line at `content_start` if it is not already a comment.

        a = 1
        ^
        content_start
        """
        if not self._is_comment(content_start):
            self._insert(self._comment_delimiter + ' ', content_start)
            return len(self._comment_delimiter) + 1
        return 0

    @read
    def uncomment(self, content_start: int, file_contents='') -> int:
        """
        Uncomment the line at `content_start` if it is a comment.

        # a = 1
          ^
          content_start
        """
        if self._is_comment(content_start):
            comment_start = self._comment_start(content_start)
            self._write(file_contents[:comment_start] + file_contents[content_start:])
            return len(self._comment_delimiter) * -1
        return 0

    def _read(self):
        content = self._io.read()
        self._io.seek(0) # position at start
        return content

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
        return substr.strip() == self._comment_delimiter

    @read
    def _comment_start(self, content_start: int, file_contents='') -> int:
        line_start = file_contents.rfind('\n', 0, content_start)
        if line_start == -1:
            line_start = 0
        else:
            line_start += 1
        return line_start
