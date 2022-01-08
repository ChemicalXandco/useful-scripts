import os

from config import firefox
from utils.config import ConfigEditor


def run():
    with ConfigEditor(os.path.join(firefox.default, 'prefs.js'), '//') as cfg_edit:
        cfg_edit.add('user_pref("browser.aboutConfig.showWarning", false);')

        # disable disk cache
        cfg_edit.add('user_pref("browser.cache.check_doc_frequency", 0);')
        cfg_edit.add('user_pref("browser.cache.disk.capacity", 0);')
        cfg_edit.add('user_pref("browser.cache.disk.content_type_media_limit", 0);')
        cfg_edit.add('user_pref("browser.cache.disk.enable", false);')
        cfg_edit.add('user_pref("browser.cache.disk.free_space_hard_limit", 0);')
        cfg_edit.add('user_pref("browser.cache.disk.free_space_soft_limit", 0);')
        cfg_edit.add('user_pref("browser.cache.disk.max_chunks_memory_usage", 0);')
        cfg_edit.add('user_pref("browser.cache.disk.max_entry_size", 0);')
        cfg_edit.add('user_pref("browser.cache.disk.max_priority_chunks_memory_usage", 0);')
        cfg_edit.add('user_pref("browser.cache.disk.metadata_memory_limit", 0);')
        cfg_edit.add('user_pref("browser.cache.disk.preload_chunk_count", 0);')
        cfg_edit.add('user_pref("browser.cache.disk.smart_size.enabled", false);')
        cfg_edit.add('user_pref("browser.cache.disk_cache_ssl", false);')

        # disable offline cache
        cfg_edit.add('user_pref("browser.cache.offline.capacity", 0);')
        cfg_edit.add('user_pref("browser.cache.offline.enable", false);')
        cfg_edit.add('user_pref("browser.cache.offline.storage.enable", false);')

        # disable sessionstore
        cfg_edit.add('user_pref("browser.sessionstore.interval", 1800000);')
        cfg_edit.add('user_pref("browser.sessionstore.max_resumed_crashes", 0);')
        cfg_edit.add('user_pref("browser.sessionstore.resume_from_crash", false);')
        cfg_edit.add('user_pref("browser.sessionstore.upgradeBackup.maxUpgradeBackups", 0);')

        # disable unneeded services
        cfg_edit.add('user_pref("extensions.pocket.enabled", false);')
        cfg_edit.add('user_pref("services.sync.prefs.sync.browser.urlbar.suggest.history", false);')

        # disable history
        cfg_edit.add('user_pref("places.history.enabled", false);')
        cfg_edit.add('user_pref("privacy.history.custom", true);')

        # urlbar
        cfg_edit.add('user_pref("browser.urlbar.maxRichResults", 1);')


if __name__ == '__main__':
    run()
