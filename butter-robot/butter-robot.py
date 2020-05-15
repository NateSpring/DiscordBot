import discord
from discord.ext import commands
from simplesms import sendtxt

TOKEN = 'NzA2ODUyNDQ4ODMyMzIzNjc0.XrATEA.vsrZkWGMt6woR-w4imFpuj72qLQ'

description = '''My purpose is to pass the butter'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Butter Robot Online')
    print(bot.user.id)
    print('------')
    
@bot.event    
async def on_message(message):
    message_info = message.content
    if message_info == "test":
        return await message.channel.send("Test recieved.")

@bot.command()
async def hello(ctx):
    """I will welcome your presence"""
    user = ctx.message.author
    await ctx.send("Hello " + user.mention + "!")

@bot.command()
async def purpose(ctx):
    """I'll explain my purpose"""
    await ctx.send("To pass the butter.")

@bot.command()
async def text(ctx, *text):
    """I'll relay your message to my master"""
    await ctx.send("Your message shall be relayed. Thank You.")
    sendtxt(" ".join(text[:]))

bot.run(TOKEN)