import discord

# 建立一個 Client 物件
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# 當機器人準備完成並上線時會執行的事件
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
    # 設定機器人正在遊玩的狀態為 "啟動保護"
    activity = discord.Game("啟動保護")
    await client.change_presence(activity=activity)

# 在這裡替換成你的機器人 Token
token = 'MTMxMzQ0ODUzMjIyMDU3OTkwMg.G1JiN2.pWdPyiRtUWO08B2U98oR6C79eKAKiW364cO3Lk'

# 啟動機器人
client.run(token)
