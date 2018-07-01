import configparser
import os
from functools import lru_cache

CONFIG_FILE_NAME = "~/.td.cfg"
CONFIG_SECTION = "settings"
DEFAULT_CONFIG = {"database_name": "todo", "editor": "vi", "order_by": "modified"}


@lru_cache()
def _get_config():
    config_file = CONFIG_FILE_NAME and os.path.expanduser(CONFIG_FILE_NAME)
    settings = DEFAULT_CONFIG
    if os.path.exists(config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        if config.has_section(CONFIG_SECTION):
            settings.update(dict(config.items(CONFIG_SECTION)))
    return settings


config = _get_config()