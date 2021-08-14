# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Cow소행성 유튜브 운영"))

@client.event
async def on_message(message):
    if message.content == "테스트": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))


# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('ODc1NjcyOTU1Njg4OTk2ODk0.YRY7_Q.p4BHzchXJPSx2J9WsLe5M1jsDXc')