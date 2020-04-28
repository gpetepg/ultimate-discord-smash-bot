"""Message based helper functions"""

import re
from ultimate_discord_smash_bot.characters import characters

def _replace_spaces_with_dashes(message):
    return message.replace(" ", "-")

def _display_matchup(message):
    message.content = message.content.replace("!matchup", "")
    foundChars = []
    for c in characters:
        if c.lower() not in message.content:
            continue
        charIndex = message.content.index(c)
        foundChars.append(c.lower())
        message.content.replace(c, "")

    if len(foundChars) != 2:
        return "You must provide only 2 characters!"

    foundChars.insert(1, "vs")
    endResult = map(_replace_spaces_with_dashes, reversed(foundChars))
    endResult = "-".join(endResult)
    return f"https://ssbworld.com/matchup/{endResult}"

def _display_data(message):
    character = re.sub('[^a-zA-Z0-9]+', ' ', ' '.join(message.content.lower().split(" ")[1:]))
    if character in characters:
        character = "_".join(message.content.split(" ")[1:])
        return f"https://ultimateframedata.com/{character}.php".lower()
    else:
        return "Could not find this character, please enter a valid character"

def _display_greeting(message):
        return f"""Hello {message.author.mention} this is our bot here are its utilities:

!data <character name> : Returns a link to a character's data.
!matchup <character 1> <character 2> : Returns a link with match up data between the two characters.
!elite : Returns a link to elite smash GSP tracker.

Source code can be found here: https://github.com/gpetepg/ultimate-discord-smash-bot
"""
