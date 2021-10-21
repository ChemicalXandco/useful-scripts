from packages.package_managers import Package, PackageList, package_manager

pkg_list = PackageList(
    Package('bat'),
    Package('bottom', apt=''),
    Package('exa'),
    Package('fd', apt='fd-find'),
    Package('ripgrep'),
    Package('starship', apt=''),
    Package('noto-fonts-emoji', apt='fonts-noto-color-emoji'),
    Package('python', apt='python3').depend(
        Package('python-lsp-server', apt='').depend(
            Package('autopep8', apt='python3-autopep8'),
            Package('flake8'),
            Package('python-mccabe', apt='python3-mccabe'),
            Package('python-pycodestyle', apt='python3-pycodestyle'),
            Package('python-pyflakes', apt='python3-pyflakes'),
            Package('python-pylint', apt='pylint'),
            Package('python-rope', apt='python3-rope'),
        ),
    ),
    Package('cargo').depend(
        Package('rust-analyzer', apt=''),
    ),
)


def run():
    packages_to_install = pkg_list.propose()

    if packages_to_install:
        print(f'Installing the following packages: {",".join(packages_to_install)}')
        package_manager.install(packages_to_install)
        print('Packages installed successfully')
