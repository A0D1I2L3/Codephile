from venv.variables import *
import discord
from discord.ext import commands

client=commands.Bot(command_prefix="?")


@client.command(name="version")
async def version(context):

    MyEmbed = discord.Embed(title="Current version" , description="The version is beta" , colour= 0x00FF00 )

    MyEmbed.add_field(name="project Name",value="project pseudobot",inline=False)
    MyEmbed.add_field(name="Date released",value="Tomorrow",inline=False)
    MyEmbed.set_footer(text="Heheheeheheheh")

    await context.message.channel.send(embed=MyEmbed)
    
        

@client.event
async def on_ready():
    general_channel = client.get_channel(947433833660317709)

    await general_channel.send('Bot online')  




client.run(TOKEN)

