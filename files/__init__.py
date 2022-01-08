import os
import urllib.request


class File:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def download(self, directory: str) -> str:
        if not os.path.isdir(directory):
            os.mkdir(directory)
        path = os.path.join(directory, self.name)
        if os.path.exists(path):
            print(f'{path} already exists, skipping download')
        else:
            print(f'downloading {self.url} to {path}')
            urllib.request.urlretrieve(url=self.url, filename=path)
        return path
