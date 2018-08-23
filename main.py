import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # user types '!foo', bot says 'bar'
    if message.content.startswith('!foo'):
        await client.send_message(destination=message.channel, content='bar')

client.run('<TOKEN>')
