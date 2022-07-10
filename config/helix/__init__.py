from config.helix import cache, common, config


def run():
    if common.supported:
        config.run()
        cache.run()
