import discord
import asyncio
 
client = discord.Client()
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
@client.event
async def on_message(message):
    if message.content.startswith('!도움말'):
        await  message.channel.send(message.channel, '저는 선웅님의 현재 상태를 나타내는 봇이에요 추후 여러가지 기능이 추가됩니다! 기대해주세요!')
 
    elif message.content.startswith('!say'):
        await  message.channel.send(message.channel, 'leave message')
        msg = await client.wait_for_message(timeout=15.0, author=message.author)
 
        if msg is None:
            await  message.channel.send(message.channel, '15초내로 입력해주세요. 다시시도: !say')
            return
        else:
            await  message.channel.send(message.channel, msg.content)
 
client.run('NzY5NzcwMzA3NjY1NjU3ODY2.X5T2dg.eYZgEelcfwkReg7252X2ZD3Zz3g')


