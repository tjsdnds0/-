import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('핑'):
      await message.delete()
      embed = discord.Embed(description=f"", colour=discord.Colour(0x594841))
      embed.set_author(name=f"현재 핑은 {int((client.latency * 1000))}'ms 입니다.")
      await message.channel.send(embed=embed)

client.run('NzY5NzcwMzA3NjY1NjU3ODY2.X5T2dg.HpueosTiUX43jLFI5qyBTdL3tTg')
