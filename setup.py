from setuptools import (
    setup,
)

setup(
    name="ultimate-discord-smash-bot",
    author='Tyler Guo',
    url=""
    version="1.0",
    description="ultimate-discord-smash-bot, A discord bot for my smash ultimate server",
    packages=[
        "ultimate_discord_smash_bot"
    ],
    package_dir={
        "ultimate_discord_smash_bot": "ultimate_discord_smash_bot",
    },
    include_package_data=True,
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "",
        ]
    },
)