import json , requests , aiohttp , nextcord , config , re , os
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def logsend(embed):
  async with aiohttp.ClientSession() as session:
    webhook = nextcord.Webhook.from_url(config.webhook, session=session)
    await webhook.send(embed=embed)
    
async def logtopup(embed):
  async with aiohttp.ClientSession() as session:
    webhook = nextcord.Webhook.from_url(config.topup_log, session=session)
    await webhook.send(embed=embed)

async def logsend1(embed1):
  async with aiohttp.ClientSession() as session:
    webhook = nextcord.Webhook.from_url(config.webhook, session=session)
    await webhook.send(embed=embed1)
    
async def logtopup1(embed1):
  async with aiohttp.ClientSession() as session:
    webhook = nextcord.Webhook.from_url(config.topup_log, session=session)
    await webhook.send(embed=embed1)

class Modal1(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(f"ป้องกันการใช้ BOT") 
        self.username = nextcord.ui.TextInput(label="ใส่อะไรก็ได้", required=True)
        self.add_item(self.username)

    async def callback(self, interaction: nextcord.Interaction):
        accdata = json.load(open('./db/acc.json', 'r'))
        accdata[str(interaction.user.id)]['point'] -= 0
        json.dump(accdata, open("./db/acc.json", "w"), indent=1)
        if self.username.value:
            role = nextcord.utils.get(interaction.guild.roles, id=1235634559748411392)
            if role in interaction.user.roles:
                embed = nextcord.Embed(description=f"โหลด -> [Download Source Code -> คลิ๊ก <-](https://cdn.discordapp.com/attachments/1235638304183947316/1235638763137531985/main.py?ex=6635c286&is=66347106&hm=748bb6c555247a83d4390552a37dc49e5ea01859aec56aaa98c61cba120a1e52&) \n หากไฟล์ Error หรือ มีปัญหา ให้แจ้งแอดมิน หรือคนที่มียศ <@&1235646549401272321> นะคะ ", color=0x77dd77)
                embed1 = nextcord.Embed(description=f"[ดูวิธีการใช้งานคลิ๊กที่นี้ -> ดู](https://www.youtube.com/watch?v=xU-B4ZLH7jg)", color=0x77dd77) 
                await logsend(nextcord.Embed(title=f"คนนี้รับโปรแกรม",description=f"คนนี้ <@{interaction.user.id}> \n\n ได้รับ EP.1 สุ่มแจก"))
                await interaction.send(embed=embed, ephemeral=True)
                await interaction.send(embed=embed1, ephemeral=True)
            else:
                embed = nextcord.Embed(description=f"เกิดข้อผิดพลาดกรุณาลองใหม่ภายหลัง " , color=0xff6961)
        else:
            await interaction.response.send_message(embed=nextcord.Embed(description=f"กรุณาแจ้ง ADMIN "), ephemeral=True)
""" class Modal2(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(f"รู้จักจากใคร") 
        self.username = nextcord.ui.TextInput(label="ชื่อ (ถ้าไม่มีให้ - เฉยๆ)", required=True)
        self.add_item(self.username)

    async def callback(self, interaction: nextcord.Interaction):
        accdata = json.load(open('./db/acc.json', 'r'))
        accdata[str(interaction.user.id)]['point'] -= 0
        json.dump(accdata, open("./db/acc.json", "w"), indent=1)
        if self.username.value:
            role = nextcord.utils.get(interaction.guild.roles, id=1235634559748411392)
            if role in interaction.user.roles:
                embed = nextcord.Embed(description=f"ไม่สำเร็จกรุณาลองใหม่อีกครั้ง :NightWolves69: ", color=0xff6961)
                await interaction.send(embed=embed, ephemeral=True)
            else:
                embed = nextcord.Embed(description=f"เข้าร้านสำเร็จยินดีต้อนรับรุ่นใหญ่", color=0x77dd77)
                await logsend(nextcord.Embed(title=f"คนเข้าร้านมาใหม่",description=f"คนนี้ <@{interaction.user.id}> \n\n รู้จักจาก {self.username.value}"))
                await interaction.user.add_roles(role)
                await interaction.send(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(embed=nextcord.Embed(description=f"กรุณากรอกชื่อ"), ephemeral=True)

class Modal3(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(f"รู้จักจากใคร") 
        self.username = nextcord.ui.TextInput(label="ชื่อ (ถ้าไม่มีให้ - เฉยๆ)", required=True)
        self.add_item(self.username)

    async def callback(self, interaction: nextcord.Interaction):
        accdata = json.load(open('./db/acc.json', 'r'))
        accdata[str(interaction.user.id)]['point'] -= 0
        json.dump(accdata, open("./db/acc.json", "w"), indent=1)
        if self.username.value:
            role = nextcord.utils.get(interaction.guild.roles, id=1235634559748411392)
            if role in interaction.user.roles:
                embed = nextcord.Embed(description=f"ไม่สำเร็จกรุณาลองใหม่อีกครั้ง :NightWolves69: ", color=0xff6961)
                await interaction.send(embed=embed, ephemeral=True)
            else:
                embed = nextcord.Embed(description=f"เข้าร้านสำเร็จยินดีต้อนรับรุ่นใหญ่", color=0x77dd77)
                await logsend(nextcord.Embed(title=f"คนเข้าร้านมาใหม่",description=f"คนนี้ <@{interaction.user.id}> \n\n รู้จักจาก {self.username.value}"))
                await interaction.user.add_roles(role)
                await interaction.send(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(embed=nextcord.Embed(description=f"กรุณากรอกชื่อ"), ephemeral=True)

class Modal4(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(f"รู้จักจากใคร") 
        self.username = nextcord.ui.TextInput(label="ชื่อ (ถ้าไม่มีให้ - เฉยๆ)", required=True)
        self.add_item(self.username)

    async def callback(self, interaction: nextcord.Interaction):
        accdata = json.load(open('./db/acc.json', 'r'))
        accdata[str(interaction.user.id)]['point'] -= 0
        json.dump(accdata, open("./db/acc.json", "w"), indent=1)
        if self.username.value:
            role = nextcord.utils.get(interaction.guild.roles, id=1235634559748411392)
            if role in interaction.user.roles:
                embed = nextcord.Embed(description=f"ไม่สำเร็จกรุณาลองใหม่อีกครั้ง :NightWolves69: ", color=0xff6961)
                await interaction.send(embed=embed, ephemeral=True)
            else:
                embed = nextcord.Embed(description=f"เข้าร้านสำเร็จยินดีต้อนรับรุ่นใหญ่", color=0x77dd77)
                await logsend(nextcord.Embed(title=f"คนเข้าร้านมาใหม่",description=f"คนนี้ <@{interaction.user.id}> \n\n รู้จักจาก {self.username.value}"))
                await interaction.user.add_roles(role)
                await interaction.send(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(embed=nextcord.Embed(description=f"กรุณากรอกชื่อ"), ephemeral=True)

class Modal5(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(f"รู้จักจากใคร") 
        self.username = nextcord.ui.TextInput(label="ชื่อ (ถ้าไม่มีให้ - เฉยๆ)", required=True)
        self.add_item(self.username)

    async def callback(self, interaction: nextcord.Interaction):
        accdata = json.load(open('./db/acc.json', 'r'))
        accdata[str(interaction.user.id)]['point'] -= 0
        json.dump(accdata, open("./db/acc.json", "w"), indent=1)
        if self.username.value:
            role = nextcord.utils.get(interaction.guild.roles, id=1235634559748411392)
            if role in interaction.user.roles:
                embed = nextcord.Embed(description=f"ไม่สำเร็จกรุณาลองใหม่อีกครั้ง :NightWolves69: ", color=0xff6961)
                await interaction.send(embed=embed, ephemeral=True)
            else:
                embed = nextcord.Embed(description=f"เข้าร้านสำเร็จยินดีต้อนรับรุ่นใหญ่", color=0x77dd77)
                await logsend(nextcord.Embed(title=f"คนเข้าร้านมาใหม่",description=f"คนนี้ <@{interaction.user.id}> \n\n รู้จักจาก {self.username.value}"))
                await interaction.user.add_roles(role)
                await interaction.send(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(embed=nextcord.Embed(description=f"กรุณากรอกชื่อ"), ephemeral=True) """


class Modal6(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(f"ป้องกันการใช้ BOT") 
        self.username = nextcord.ui.TextInput(label="ใส่อะไรก็ได้", required=True)
        self.add_item(self.username)

    async def callback(self, interaction: nextcord.Interaction):
        accdata = json.load(open('./db/acc.json', 'r'))
        accdata[str(interaction.user.id)]['point'] -= 0
        json.dump(accdata, open("./db/acc.json", "w"), indent=1)
        if self.username.value:
            role = nextcord.utils.get(interaction.guild.roles, id=1235634559748411392)
            if role in interaction.user.roles:
                embed = nextcord.Embed(description=f"โหลด -> [Download Source Code -> คลิ๊ก <-](https://cdn.discordapp.com/attachments/1235638304183947316/1235638763137531985/main.py?ex=6635c286&is=66347106&hm=748bb6c555247a83d4390552a37dc49e5ea01859aec56aaa98c61cba120a1e52&) \n หากไฟล์ Error หรือ มีปัญหา ให้แจ้งแอดมิน หรือคนที่มียศ <@&1235646549401272321> นะคะ ", color=0x77dd77)
                embed1 = nextcord.Embed(description=f"[ดูวิธีการใช้งานคลิ๊กที่นี้ -> ดู](https://www.youtube.com/watch?v=xU-B4ZLH7jg)", color=0x77dd77) 
                await logsend(nextcord.Embed(title=f"คนนี้รับโปรแกรม",description=f"คนนี้ <@{interaction.user.id}> \n\n ได้รับ EP.1 สุ่มแจก"))
                await interaction.send(embed=embed, ephemeral=True)
                await interaction.send(embed=embed1, ephemeral=True)
            else:
                embed = nextcord.Embed(description=f"เกิดข้อผิดพลาดกรุณาลองใหม่ภายหลัง " , color=0xff6961)
        else:
            await interaction.response.send_message(embed=nextcord.Embed(description=f"กรุณาแจ้ง ADMIN "), ephemeral=True)

            
class Menu(nextcord.ui.Select):
    def __init__(self):
      options = [
        nextcord.SelectOption(label='โค้ดของรายการสุ่มแจก',description='โค้ดของ สุ่มแจก EP.1 ',value='1'),
      ]
      super().__init__(custom_id='menu',placeholder='เลือกโค้ดที่คุณต้องการ',options=options)
    async def callback(self, interaction: nextcord.Interaction):
        type = self.values[0]
        money = json.load(open('./db/acc.json'))[str(interaction.user.id)]['point']
        if type == '6':
            need = 0 - money
            if money < 0:
             await interaction.send(f'มีเงินไม่พอ ต้องการ 50 บาท (ขาดอีก {need} บาท)',ephemeral=True)
             return 
            else:
             await interaction.response.send_modal(Modal1())


class Menu1(nextcord.ui.Select):
    def __init__(self):
      options = [
        nextcord.SelectOption(label='โค้ดของรายการสุ่มแจก',description='โค้ดของ สุ่มแจก EP.1 ',value='6'),
      ]
      super().__init__(custom_id='menu',placeholder='เลือกโค้ดที่คุณต้องการ',options=options)
    async def callback(self, interaction: nextcord.Interaction):
        type = self.values[0]
        money = json.load(open('./db/acc.json'))[str(interaction.user.id)]['point']
        if type == '6':
            need = 0 - money
            if money < 0:
             await interaction.send(f'มีเงินไม่พอ ต้องการ 50 บาท (ขาดอีก {need} บาท)',ephemeral=True)
             return 
            else:
             await interaction.response.send_modal(Modal6())


class Button(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label='กดเพื่อรับโปรแกรม', style=nextcord.ButtonStyle.green, emoji='🛒',custom_id="buy")
    async def buy(self, button: nextcord.Button, interaction: nextcord.Interaction):
        if check(interaction.user.id) == False or True:
            await interaction.send(embed=nextcord.Embed(description=f"**```Donwload Code ของรายการ สุ่มแจก```**",color=0xFFFF00),view=Select1(),ephemeral=True)


class Button1(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label='กดเพื่อรับโปรแกรม', style=nextcord.ButtonStyle.green, emoji='🛒',custom_id="buy")
    async def buy(self, button: nextcord.Button, interaction: nextcord.Interaction):
        if check(interaction.user.id) == False or True:
            await interaction.send(embed=nextcord.Embed(description=f"**```Donwload Code ของรายการ สุ่มแจก```**",color=0xFFFF00),view=Select1(),ephemeral=True)



class Select(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Menu())

class Select1(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Menu1())
           
      
@bot.event
async def on_ready():
    bot.add_view(Button())
    print(f"BOT NAME : {bot.user}")


@bot.slash_command(guild_ids=[config.guild_id],description=f"setup")
async def setup(interaction: nextcord.Interaction):
        await interaction.channel.send(embed=nextcord.Embed(description=f"**```โค้ดจากรายการสุ่มแจก```**",color=0xFFFF00).set_image(url='https://media.discordapp.net/attachments/1236018604940595283/1236018657784762468/image_5.png?ex=66367b94&is=66352a14&hm=a3a9321bab84f10beb99001e317a7f5597b9eba3d73ec168faeb82d31bd20f66&=&format=webp&quality=lossless&width=350&height=350'),view=Button1())
        await interaction.send('สำเร็จ!',ephemeral=True)

@bot.slash_command(guild_ids=[config.guild_id],description=f"setupshop")
async def setupshop(interaction: nextcord.Interaction):
        await interaction.channel.send(embed=nextcord.Embed(description=f"**```โค้ดจากรายการสุ่มแจก```**",color=0xFFFF00).set_image(url='https://media.discordapp.net/attachments/1236018604940595283/1236018657784762468/image_5.png?ex=66367b94&is=66352a14&hm=a3a9321bab84f10beb99001e317a7f5597b9eba3d73ec168faeb82d31bd20f66&=&format=webp&quality=lossless&width=350&height=350'),view=Button1())
        await interaction.send('สำเร็จ!',ephemeral=True)
    
def check(id):
    accdata = json.load(open('./db/acc.json', 'r'))
    if str(id) in accdata:
        print(f'{id} in db')
        return True
        
    else:
        print(f'{id} not in db')
        accdata[id] = {
            "point" : 0,
            "pointall" : 0
        }
        json.dump(accdata, open("./db/acc.json", "w"), indent = 4)

bot.run(config.token)
