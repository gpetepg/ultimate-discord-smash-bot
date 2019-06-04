# Work with Python 3.6
import discord
from discord.utils import get
from credentials import TOKEN

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
        greetings = "Hello {0.author.mention} this is our bot here are its options".format(message)
        await message.channel.send(greetings)

    # Don't need to check if the user already has the "Verified" role, if they already have it nothing will happen.
    if (message.channel == client.get_channel(_introduction_channel_id)) and (len(message.content) > 20 ):
        role = discord.utils.get(message.guild.roles, id=_verified_role_id)
        await message.author.add_roles(role)

@client.event
async def on_member_join(member):
    """ When a member joins send them a DM.
    """

    msg = """Hello {0.display_name}. Welcome to our Smash Ultimate Discord.
Please go to the #Introduction channel and in ONE MESSAGE please message with the following format here: 
    - Name 
    - Whose friend you are or who invited you 
    - Nintendo friend code """.format(member)
    await member.send(msg)


@client.event
async def on_ready():
    print(f"""Logged in as...
Client Username: {client.user.name}
Client ID: {client.user.id}
------""")

client.run(TOKEN)
