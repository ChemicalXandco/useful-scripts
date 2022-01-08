from abc import ABC, abstractmethod
from subprocess import CalledProcessError

from utils.env import is_exe, run
from utils.ui import yesno


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
        if previous_response is not None:
            self.to_install = previous_response
            return previous_response

        response = yesno(f'Install {self.name}?')
        self.to_install = response.result
        return self.to_install if response.all else None

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


class Alpine(PackageManager):
    name = 'apk'
    root = True


class Arch(PackageManager):
    name = 'pacman'
    root = True

    def install(self, packages: list[str]):
        run('sudo', self.name, '-Sy', '--noconfirm', *packages)

    def is_installed(self, package: str) -> bool:
        try:
            run(self.name, '-Q', package)
            return True
        except CalledProcessError:
            return False


class Brew(PackageManager):
    name = 'brew'
    root = False

    def install(self, packages: list[str]):
        for package in packages:
            run(self.name, 'install', package)

    def is_installed(self, package: str) -> bool:
        try:
            return len(run(self.name, 'ls', '--versions', package)) > 0
        except CalledProcessError:
            return False


class Debian(PackageManager):
    name = 'apt'
    root = True

    def install(self, packages: list[str]):
        run('sudo', self.name, 'install', '-y', *packages)

    def is_installed(self, package: str) -> bool:
        try:
            run('dpkg', '-l', package)
            return True
        except CalledProcessError:
            return False


class Gentoo(PackageManager):
    name = 'emerge'
    root = True

    def install(self, packages: list[str]):
        run('sudo', self.name, *packages)


class NixOS(PackageManager):
    name = 'nix-env'
    root = True


class OpenSUSE(PackageManager):
    name = 'zypper'
    root = True


class RH(PackageManager):
    name = 'dnf'
    root = True


available_package_managers = (
    Alpine,
    Arch,
    Brew,
    Debian,
    Gentoo,
    NixOS,
    OpenSUSE,
    RH,
)

for i in available_package_managers:
    if is_exe(i.name):
        package_manager = i()
        break

if not package_manager:
    raise RuntimeError('could not find a package manager')
print(f'found package manager {package_manager}')
