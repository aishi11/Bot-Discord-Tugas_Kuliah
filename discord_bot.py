import discord
from discord.ext import commands
from commands import TaskBot
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
taskbot = TaskBot()

@bot.event
async def on_ready():
    print(f'{bot.user} telah masuk sebagai bot!')

@bot.command()
async def tambah(ctx, *, deskripsi):
    task = taskbot.add_task(deskripsi)
    await ctx.send(f'Tugas ditambahkan: {task["id"]}. {task["desc"]}')

@bot.command()
async def hapus(ctx, task_id: int):
    success = taskbot.delete_task(task_id)
    await ctx.send("Tugas berhasil dihapus!" if success else "Tugas tidak ditemukan.")

@bot.command()
async def tandai(ctx, task_id: int):
    success = taskbot.mark_done(task_id)
    await ctx.send("Tugas ditandai selesai!" if success else "Tugas tidak ditemukan.")

@bot.command()
async def list(ctx):
    tugas = taskbot.list_tugas()
    await ctx.send(tugas)

def run_discord_bot():
    bot.run(TOKEN)
