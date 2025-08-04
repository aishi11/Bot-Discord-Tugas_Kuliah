import sqlite3
from commands import TaskBot

def test_delete_task(tmp_path):
    db_file = tmp_path / "tugas_kuliah.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE tugas_kuliah (task_id INTEGER PRIMARY KEY, judul_tugas TEXT, completed BOOLEAN)")
    cursor.execute("INSERT INTO tugas_kuliah (judul_tugas, completed) VALUES ('Test delete', 0)")
    conn.commit()

    bot = TaskBot()
    bot.conn, bot.cursor = conn, cursor

    bot.delete_task(1)
    cursor.execute("SELECT * FROM tugas_kuliah WHERE task_id = 1")
    assert cursor.fetchone() is None
