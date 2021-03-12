import discord
import random
TOKEN = 'NzY5NzcwMzA3NjY1NjU3ODY2.X5T2dg.HpueosTiUX43jLFI5qyBTdL3tTg' 

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('+검색 '):
        message.content = "https://search.naver.com/search.naver?query="+message.content.replace("+검색 ","").replace(" ","%20")
        msg = message.content
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------------------------')
    print('접속 성공! 안녕하세요 선웅님!')

client.run ("NzY5NzcwMzA3NjY1NjU3ODY2.X5T2dg.HpueosTiUX43jLFI5qyBTdL3tTg")