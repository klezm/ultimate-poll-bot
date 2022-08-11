"""Config values for pollbot."""
import logging
import os
import sys

import toml

assert os.environ.get("BOT_NAME"), "Set the variable as secrets in GitHub"
assert os.environ.get("BOT_API_KEY"), "Set the variable as secrets in GitHub"

default_config = {
    "telegram": {
        # Set these two variables as secrets in GitHub
        "bot_name": os.environ["BOT_NAME"],
        "api_key": os.environ["BOT_API_KEY"],
        "worker_count": 20,
        "admin": "nukesor",
        "allow_private_vote": False,
        "max_user_votes_per_day": 200,
        "max_inline_shares": 20,
        "max_polls_per_user": 200,
    },
    "database": {
        # "sql_uri": "postgresql://pollbot:localhost/pollbot",
        "sql_uri": "postgresql://vscode@localhost/vscode",
        "connection_count": 20,
        "overflow_count": 10,
    },
    "logging": {
        "sentry_enabled": False,
        "sentry_token": "",
        "log_level": logging.INFO,
        "debug": False,
    },
    "webhook": {
        "enabled": False,
        "domain": "https://localhost",
        # "token": "pollbot",
        "token": "vscode",
        # "cert_path": "/path/to/cert.pem",
        # "port": 7000,
        "port": 5432,
    },
}

config_path = os.path.expanduser("~/.config/ultimate_pollbot.toml")

if not os.path.exists(config_path):
    with open(config_path, "w") as file_descriptor:
        toml.dump(default_config, file_descriptor)
    print("Please adjust the configuration file at '~/.config/ultimate_pollbot.toml'")
    sys.exit(1)
else:
    config = toml.load(config_path)

    # Set default values for any missing keys in the loaded config
    for key, category in default_config.items():
        for option, value in category.items():
            if option not in config[key]:
                config[key][option] = value
