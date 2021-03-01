import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong {round(client.latency * 1000)}ms')

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount):
    amount = int(amount)
    await ctx.channel.purge(limit=amount+1)

client.run('token')