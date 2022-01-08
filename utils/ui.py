import os
from typing import Union

from files import File, wallpapers
from utils.env import dotfile_path


def browse(f_list) -> Union[File, None]:
    directory = isinstance(f_list, dict)
    if directory:
        opts = f_list.keys()
    else:
        opts = [f.name for f in f_list]
    while True:
        selection = select(*opts, back=True)
        if not selection:
            return None
        if directory:
            sub = browse(f_list[selection])
            if sub:
                return sub
            continue
        for f in f_list:
            if f.name == selection:
                return f


def get_bg(default_files: list[str] = []):
    base_opts = [
                'select from database of online backgrounds',
                'manually input url',
                'input path of local file',
                ]
    if default_files:
        base_opts.append('select from default backgrounds provided by the window manager')
    while True:
        print('Where to find background?')
        src = select(*base_opts)
        idx = base_opts.index(src)
        if idx in range(2):
            if idx == 0:
                f = browse(wallpapers.f_list)
            else:
                f_url = input('url (enter to go back): ')
                if not f_url:
                    continue
                f_name = input_with_default('filename', os.path.basename(f_url))
                f = File(name=f_name, url=f_url)

            if not f:
                continue
            return f.download(dotfile_path('Pictures/Wallpapers'))
        elif idx == 2:
            path = input('local path (enter to go back): ')
            if not path:
                continue
            return path
        elif idx == 3:
            path = select(*default_files, back=True)
            if not path:
                continue
            return path


def input_with_default(prompt, default):
    response = input(f'{prompt} (default {default}): ')
    if not response:
        response = default
    return response


def select(*options: list[str], back: bool = False, default: str = '') -> str:
    options = list(options)
    if back:
        options.append('[go back]')
    while True:
        print('select from the following list:')
        for i, opt in enumerate(options):
            print(f'{i} - {opt}')

        prompt = f'0-{len(options)-1}'
        if default:
            prompt += f' (default {default})'
        prompt += ': '
        selection = input(prompt)

        if selection == '' and default:
            print(f'selecting default option {default}')
            return default
        try:
            result = options[int(selection)]
            print(f'selecting option {selection}: {result}')
        except ValueError:
            if selection in options:
                result = selection
            else:
                print(f'Invalid option {selection}')
                continue
        except IndexError:
            print(f'{selection} out of range')
            continue

        if result == '[go back]':
            return ''
        return result


class YesNoResult:
    def __init__(self, result: bool):
        self.result = result
        self.all = False


def yesno(prompt: str, repeat: bool = False) -> YesNoResult:
    options = 'y/ya/n/na' if repeat else 'y/n'
    max_len = 2 if repeat else 1
    while True:
        response = input(f'{prompt} ({options}):')

        if response[0] == 'y':
            result = YesNoResult(True)
        elif response[0] == 'n':
            result = YesNoResult(False)
        else:
            print(f'Invalid input "{response}"')
            continue

        if len(response) > max_len:
            print(f'Input "{response}" invalid: too many characters')
            continue
        elif len(response) == 2 and response[1] == 'a':
            result.all = True
        elif len(response) == 2:
            print(f'Input "{response}" invalid: {response[1]} is not a valid character')
            continue

        return result
