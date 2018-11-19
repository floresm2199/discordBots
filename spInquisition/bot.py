import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='si.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def nhentai(ctx, a: str):
    await bot.say("https://nhentai.net/g/" + a )

@bot.command(pass_context=True)
async def nobodyExpects(ctx):
    await bot.say("Nobody expects the Spanish Inquisition!")
    await bot.say("https://youtu.be/vt0Y39eMvpI?t=44s")

@bot.command(pass_context=True)
async def greet(ctx):
    await bot.say("Hello, there!")

@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.say(latency)

@bot.command(pass_context = True)
async def talk(ctx):
    converse = 1
    while(converse == 1):
        text = input("Put text here: ")
        if(text == "stop()"):
            converse = 0
        if(converse == 1):
            await bot.say(text)

@bot.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="hiro#4359")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=489100860329295882&permissions=0&scope=bot)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="The Spanish Inquisition", description="A bot that nobody expects", color=0xeee657)

bot.run('Insert token here')
