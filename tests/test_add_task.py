import os
import sqlite3
import pytest
from commands import TaskBot

@pytest.fixture
def bot():
    if os.path.exists("test_tugas_kuliah.db"):
        os.remove("test_tugas_kuliah.db")
    bot = TaskBot()
    bot.conn, bot.cursor = sqlite3.connect("test_tugas_kuliah.db"), sqlite3.connect("test_tugas_kuliah.db").cursor()
    bot.cursor.execute("CREATE TABLE tugas_kuliah (task_id INTEGER PRIMARY KEY, judul_tugas TEXT, completed BOOLEAN)")
    return bot

def test_add_task(bot):
    bot.add_task("Write tests")
    bot.cursor.execute("SELECT judul_tugas FROM tugas_kuliah WHERE judul_tugas = 'Write tests'")
    result = bot.cursor.fetchone()
    assert result is not None
