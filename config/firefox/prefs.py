import os

from config import firefox
from utils.config import ConfigEditor

def run():
    with ConfigEditor(os.path.join(firefox.default, 'prefs.js'), '//') as cfg_edit:
        cfg_edit.add('user_pref("browser.cache.disk.enable", false);', under='user_pref("browser.bookmarks.showMobileBookmarks", true);')

if __name__ == '__main__':
    run()
