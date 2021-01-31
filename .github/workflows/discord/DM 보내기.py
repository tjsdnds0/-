import discord

client = discord.Client()

@client.event
if message.content == "!설명":
            if message.author.dm_channel:
                await message.author.dm_channel.send("DM 채널이 있어서 그냥 보냈어요!")
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()
                await channel.send("DM 채널이 없어서 만들고 보냈어요!")

client.run('NzY5NzcwMzA3NjY1NjU3ODY2.X5T2dg.eYZgEelcfwkReg7252X2ZD3Zz3g')