import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

# 1. Tạo Web Server nhỏ bằng Flask để Render không tắt bot
app = Flask('')

@app.route('/')
def home():
    return "Bot Discord đang hoạt động 24/7!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. Cấu hình Bot Discord
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Đã đăng nhập thành công bot: {bot.user}')

# Chạy web server trước khi chạy bot
keep_alive()

# Nhớ thay TOKEN_CỦA_BẠN bằng token thật lấy từ Discord Developer Portal
TOKEN = os.environ.get("DISCORD_TOKEN", "TOKEN_CỦA_BẠN")
bot.run(TOKEN)
