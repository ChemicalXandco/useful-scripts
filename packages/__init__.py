from packages.package_managers import Package, PackageList

pkg_list = PackageList(
    Package('bat'),
    Package('exa'),
    Package('fd', apt='fd-find'),
    Package('ripgrep'),
    Package('starship', apt=''),
)

def run():
    pkg_list.install()
