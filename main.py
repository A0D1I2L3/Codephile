from venv.variables import *
import discord
from discord.ext import commands
from random import randint

client=commands.Bot(command_prefix="cd ")


@client.command(name="version")
async def version(context):

    MyEmbed = discord.Embed(title="Current version" , description="The version is beta" , colour= 0x00FF00 )

    MyEmbed.add_field(name="project Name",value="project pseudobot",inline=False)
    MyEmbed.add_field(name="Date released",value="Tomorrow",inline=True)
    MyEmbed.set_footer(text="Heheheeheheheh")

    await context.message.channel.send(embed=MyEmbed)
    
@client.command(name="dice")
async def version(context):
    i=randint(1,6)
    await context.message.channel.send("Bot rolled :game_die:  " + str(i))
    

@client.command(name="status")
async def test(context):
    await context.message.channel.send('Bot online')  


@client.command(name="welp")
async def help(context):
    myEmbed=discord.Embed(title="Codephile",description=" All The Commands for Codephile",colour=0x00FF00)
    myEmbed.add_field(name=":robot: General",value="`cd status`:- Display bot status \n `cd version`:- Display bot version",inline=False,)
    myEmbed.add_field(name=":sparkles: Fun",value="`cd dice`:- Bot will roll a dice for you",inline="False")

    await context.message.channel.send(embed=myEmbed)

client.run(TOKEN)

