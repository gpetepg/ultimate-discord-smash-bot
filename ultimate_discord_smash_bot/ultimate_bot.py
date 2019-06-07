# Work with Python 3.6
import discord
import re
from discord.utils import get
from credentials import TOKEN
from characters import characters

TOKEN = TOKEN

client = discord.Client()

@client.event
async def on_message(message):
    """ Messaged based events
    """
    
    _introduction_channel_id = 521771464668610561
    _verified_role_id = 585273441058553866

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith("!bot"):
        greetings = f"""Hello {message.author.mention} this is our bot here are its utilities:

!data <character name> : Returns a link to a character's data.
!matchup <character 1> <character 2> : Returns a link with match up data between the two characters.
"""
        await message.channel.send(greetings)

    # @ToDo Create this logic
    if message.content.startswith("!matchup"):
        matchup_message = display_matchup(message)
        await message.channel.send(matchup_message)


    if message.content.startswith("!data"):
        # separate the !data from the message content and clear out any delimeters with spaces then check the list...
        character = re.sub('[^a-zA-Z0-9]+', ' ', ' '.join(message.content.split(" ")[1:]))
        if character in characters:
            character = "_".join(message.content.split(" ")[1:])
            character_data = f"https://ultimateframedata.com/{character}.php"
            await message.channel.send(character_data)
        else:
            await message.channel.send("Could not find this character, please enter a valid character")

    # Don't need to check if the user already has the "Verified" role, if they already have it nothing will happen.
    if (message.channel == client.get_channel(_introduction_channel_id)) and (len(message.content) > 20 ):
        role = discord.utils.get(message.guild.roles, id=_verified_role_id)
        await message.author.add_roles(role)

@client.event
async def on_member_join(member):
    """ When a member joins send them a DM.
    """

    msg = f"""Hello {member.display_name}. Welcome to our Smash Ultimate Discord.
Please go to the #Introduction channel and in ONE MESSAGE please message with the following format here: 
    - Name 
    - Whose friend you are or who invited you 
    - Nintendo friend code"""
    await member.send(msg)

def replace_spaces_with_dashes(message):
    return message.replace(" ", "-")

def display_matchup(message):
    message.content = message.content.replace("!matchup", "")
    foundChars = []
    for c in characters:
        if c not in message.content:
            continue
        charIndex = message.content.index(c)
        foundChars.append(c)
        message.content.replace(c, "")
    if len(foundChars) != 2:
        return "You must provide only 2 characters!"
        return
    foundChars.insert(1, "vs")
    endResult = map(replace_spaces_with_dashes, reversed(foundChars))
    endResult = "-".join(endResult)
    url = f"https://ssbworld.com/matchup/{endResult}"
    return url

@client.event
async def on_ready():
    print(f"""Logged in as...
Client Username: {client.user.name}
Client ID: {client.user.id}
------""")

client.run(TOKEN)
