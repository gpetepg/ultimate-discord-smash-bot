# ultimate-discord-smash-bot
Bot we made for our Smash Ultimate discord server.

Only dependancy is [`discord`](https://github.com/Rapptz/discord.py) but I've included a `requiements.txt` regardless. I'll probably add dismock which is mentioned below too for testing.

You will need to provide your own servers token imported from `credentials.py`.

##### Quickstart #####

Basic setup using `bash` and `GNU Make`. I recommend using a [virtual environment](https://docs.python.org/3/library/venv.html) anyway if you chose to not use the `.env` or `Makefile`.

    git clone git@github.com:gpetepg/ultimate-discord-smash-bot.git
    source setup.env
    make
    source ve/bin/activate
    pip install -r requirements.txt
    python3 ultimate_bot.py
    
To run tests

    make _test

Official discord api documentation:
https://discordpy.readthedocs.io/en/latest/index.html

NOTE: If you are using `python3.6` on `Mac OS X` There is a known SSL issue which will give you trouble when trying to authenticate with Discord. Run the shell scripts provided in `python3.6_ssl_error_scripts/` to address this.
    
    sh Install Certificates.command
    sh Update Shell Profile.command

TODO:
 - [Bot to bot testing](https://github.com/DXsmiley/dismock)
