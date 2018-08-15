import discord
from discord.ext import commands
import asyncio
from itertools import cycle

token = 'NDYzNDgyNzQ4MzAxMjEzNzA2.Dixy7w.5JILo_w38M55rl4LcDsXkGjAKyQ'
client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!:ping_pong: Bot latency : {} ms'.format(client.latency * 1000))

@client.command()
async def wet(ctx):
    await ctx.send('Drip:sweat_drops:')

@client.command(pass_context = True)
async def clear(ctx, number):
    if ctx.message.author.guild_permissions.administrator:
            channel = ctx.message.channel
            mgs = []
            number = int(number)
            async for message in channel.history(limit = number + 1):
                mgs.append(message)
            await channel.delete_messages(mgs)
    else:
        channel = ctx.message.channel
        mgs = []
        number = int(1)
        async for message in channel.history(limit = number):
            mgs.append(message)
        await channel.delete_messages(mgs)
        permission_error = str('Sorry you do not have permissions to do that!')
        await ctx.send(ctx.message.channel, permission_error)

client.run(token)
