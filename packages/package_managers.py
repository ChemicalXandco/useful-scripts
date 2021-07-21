from abc import ABC, abstractmethod
from subprocess import CalledProcessError

from utils.env import is_exe, run


class PackageList:
    def __init__(self, *packages):
        self._packages = packages

    def propose(self):
        previous_response = None
        packages_to_install = []
        for i in self._packages:
            previous_response = i.propose(previous_response)
            if i.to_install:
                packages_to_install.append(i.name)
            if i.to_install or (i.installed and i.name):
                packages_to_install += i.depends.propose()
        return packages_to_install

    def add(self, *packages):
        self._packages += packages


class Package:
    def __init__(self, name, **kwargs):
        self.name = kwargs.get(package_manager.name, name)
        self.depends = PackageList()

    @property
    def installed(self):
        if not self.name:
            return True  # fake being installed so that this package is ignored
        else:
            return package_manager.is_installed(self.name)

    def propose(self, previous_response: None):
        if self.installed:
            self.to_install = False
            return previous_response
        if previous_response != None:
            self.to_install = previous_response
            return previous_response

        valid_response = False
        while not valid_response:
            response = input(f'Install {self.name}? (y/ya/n/na)')

            if response[0] == 'y':
                self.to_install = True
                valid_response = True
            elif response[0] == 'n':
                self.to_install = False
                valid_response = True
            else:
                print(f'Invalid input "{response}"')

            if len(response) > 2:
                print(f'Input "{response}" invalid: too many characters')
                valid_response = False
            elif len(response) == 2 and response[1] == 'a':
                return self.to_install
            elif len(response) == 2:
                print(f'Input "{response}" invalid: {response[1]} is not a valid character')
                valid_response = False

        return None

    def depend(self, *args):
        self.depends.add(*args)
        return self


class PackageManager(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def install(self, packages: list[str]):
        pass

    @abstractmethod
    def is_installed(self, package: str) -> bool:
        pass


class Arch(PackageManager):
    name = 'pacman'

    def install(self, packages: list[str]):
        run('sudo', self.name, '-Sy', '--noconfirm', *packages)

    def is_installed(self, package: str) -> bool:
        try:
            run(self.name, '-Q', package)
            return True
        except CalledProcessError:
            return False


class Debian(PackageManager):
    name = 'apt'

    def install(self, packages: list[str]):
        run('sudo', self.name, 'install', '-y', *packages)

    def is_installed(self, package: str) -> bool:
        try:
            run('dpkg', '-l', package)
            return True
        except CalledProcessError:
            return False


class RH(PackageManager):
    name = 'dnf'


class NixOS(PackageManager):
    name = 'nix-env'


class Gentoo(PackageManager):
    name = 'emerge'

    def install(self, packages: list[str]):
        run('sudo', self.name, *packages)


class Alpine(PackageManager):
    name = 'apk'


class OpenSUSE(PackageManager):
    name = 'zypper'

available_package_managers = (
    Arch,
    Debian,
    RH,
    NixOS,
    Gentoo,
    Alpine,
    OpenSUSE,
)

for i in available_package_managers:
    if is_exe(i.name):
        package_manager = i()
        break

if not package_manager:
    raise RuntimeError('Unknown package manager')
