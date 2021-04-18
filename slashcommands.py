import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

guild_ids = ['guild id']

@client.event
async def on_ready():
    print('Bot is ready.')

@slash.slash(name="test", description="a test command", guild_ids=guild_ids)
async def _test(ctx: SlashContext):
    embed=discord.Embed(title="Test Embed", description="just a test ya know", color=0x33ffb1)
    embed.set_author(name="Test Embed", url='https://i.imgur.com/fie9KiY.png', icon_url='https://i.imgur.com/fie9KiY.png')
    embed.set_thumbnail(url='https://i.imgur.com/fie9KiY.png')
    embed.add_field(name="Test Header", value="Test Description", inline=True)
    embed.add_field(name="Test Header 2", value="Test Description 2", inline=True)
    embed.add_field(name="Test Header 3", value="Test Description 3", inline=True)
    embed.add_field(name="Test Header 4", value="Test Description 4", inline=True)
    embed.set_footer(text="Footer Text")

    await ctx.send(content="test", embeds=[embed])

@slash.slash(name="help", description="returns you commands and description of them", guild_ids=guild_ids)
async def _help(ctx: SlashContext):
    await ctx.respond()
    await ctx.send("can't really help you here unfortunately")

@slash.slash(name="tryitandsee", description="just try it and see... i guess?", guild_ids=guild_ids)
async def _tryitandsee(ctx: SlashContext):
    await ctx.respond()
    await ctx.send("https://tryitands.ee/")

@slash.slash(name="heartattack", description="everybody just droppin like flies", guild_ids=guild_ids)
async def _heartattack(ctx: SlashContext):
    await ctx.respond()
    await ctx.send("https://youtu.be/8tP4V0tH-bA")

@slash.slash(name="luke", description="the crisp", guild_ids=guild_ids)
async def _luke(ctx: SlashContext):
    await ctx.respond()
    await ctx.send("https://i.imgur.com/fie9KiY.png")

client.run('token')
