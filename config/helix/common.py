import platform

from utils.env import dotfile_path

supported = True
if platform.system() in ['Linux', 'Darwin']:
    root = dotfile_path('.config/helix')
    cache_dir = dotfile_path('.cache/helix')
elif platform.system() == 'Windows':
    root = dotfile_path('AppData/Roaming/helix')
    cache_dir = dotfile_path('AppData/Local/helix')
else:
    supported = False
