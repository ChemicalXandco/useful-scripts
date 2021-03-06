from packages.definitions import Package, PackageChoice, PackageList

browser_web = PackageChoice(
    Package('firefox'),
    Package('chromium'),
)

all = [
    browser_web,
]


def add(base: PackageList, desktop: bool = False):
    """
    can only be ran from `./desktops.py`
    if ran at module level there is no knowledge of if a desktop enviroment is installed
    """
    if not desktop:
        return

    for i in all:
        base.add(i)
