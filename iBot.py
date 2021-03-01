import discord


client = discord.Client()


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        if str(message.author) == "iDawg#1111":
            await message.channel.send("Hey asshole, I'm reborn in Python.")
        else:
            await message.channel.send("Hey asshole, I'm reborn in Python.")


client.run('token')
