import discord
from discord.ext import commands
from commands import TaskBot
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix='!', intents=intents)
taskbot = TaskBot()

@bot.event
async def on_ready():
    print(f'{bot.user} telah masuk sebagai bot!')

@bot.command()
async def add_task(ctx, *, judul_tugas):
    task = taskbot.add_task(judul_tugas)
    await ctx.send(f'Tugas ditambahkan: {task["task_id"]}. {task["judul_tugas"]}')

@bot.command()
async def delete_task(ctx, task_id: int):
    success = taskbot.delete_task(task_id)
    await ctx.send("Tugas berhasil dihapus!" if success else "Tugas tidak ditemukan.")

@bot.command()
async def complete_task(ctx, task_id: int):
    result = taskbot.mark_done(task_id)
    if result == "marked":
        await ctx.send("Tugas ditandai selesai!")
    elif result == "already_done":
        await ctx.send("Tugas sudah ditandai selesai.")
    else:
        await ctx.send("Tugas tidak ditemukan.")

@bot.command()
async def show_tasks(ctx):
    tugas = taskbot.list_tugas()
    await ctx.send(tugas)

def run_discord_bot():
    bot.run(TOKEN)

if __name__ == "__main__":
    run_discord_bot()