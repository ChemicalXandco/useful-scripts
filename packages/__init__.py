from packages.package_managers import Package, PackageList

pkg_list = PackageList(
    Package('bat'),
    Package('exa'),
    Package('fd', apt='fd-find'),
    Package('ripgrep'),
    Package('starship', apt=''),
    Package('noto-fonts-emoji', apt='fonts-noto-color-emoji'),
)

def run():
    pkg_list.install()
