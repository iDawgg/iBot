import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())
slash = SlashCommand(client)

@client.event
async def on_ready():
    print('Bot is ready.')

@slash.slash(name="test")
async def _test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])

client.run('token')