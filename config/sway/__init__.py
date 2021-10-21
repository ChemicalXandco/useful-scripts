from config.sway import env, main_config
from utils.env import dotfile_path

root = dotfile_path('.config/sway')


def run():
    env.run()
    main_config.run()
