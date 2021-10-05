import discord
import os
import re
intents = discord.Intents().all()
client = discord.Client(command_prefix=',', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!getbots'):
        x = []

        for guild in client.guilds:
            name = str(guild) + '.txt'
            file1 = open(name,"w")
            async for member in guild.fetch_members(limit=None):
                if re.search(r'[a-zA-Z]+\d{7}', member.name):
                    x.append(str(member))
            for i in range(len(x)):
                file1.write(str(x[i] + '\n'))
                file1.close
            for i in range (len(x)):
                str1 = ''
                rng = 5
                if len(x)-rng*i>rng:
                    for z in range(rng):
                        numberNow = z + i*rng
                        str1 += str(x[numberNow] + '\n')
                else:
                    for z in range(len(x)-rng*i):
                        numberNow = z + i*rng
                        str1 += str(x[numberNow] + '\n')
                if str1 != '':
                    await message.channel.send('potential bot list: ```css\n' + str1 + '```')


client.run(os.getenv('TOKEN'))
