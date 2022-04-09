from venv.variables import *
import discord

client=discord.Client()


@client.event
async def on_ready():
    general_channel = client.get_channel(947433833660317709)

    await general_channel.send('Bot online')  


@client.event
async def on_message(message):

    if message.content.startswith ("!version"):
        general_channel = client.get_channel(947433833660317709)

        MyEmbed = discord.Embed(title="Current version" , description="The version is beta" , colour= 0x00FF00 )

        MyEmbed.add_field(name="project Name",value="project pseudobot",inline=False)
        MyEmbed.add_field(name="Date released",value="Tomorrow",inline=False)
        MyEmbed.set_footer(text="Heheheeheheheh")
        




        await general_channel.send(embed=MyEmbed) 

client.run(TOKEN)

