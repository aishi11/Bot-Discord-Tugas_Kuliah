import sqlite3
from commands import TaskBot

def test_mark_done(tmp_path):
    db_file = tmp_path / "tugas_kuliah.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE tugas_kuliah (task_id INTEGER PRIMARY KEY, judul_tugas TEXT, completed BOOLEAN)")
    cursor.execute("INSERT INTO tugas_kuliah (judul_tugas, completed) VALUES ('Complete me', 0)")
    conn.commit()

    bot = TaskBot()
    bot.conn, bot.cursor = conn, cursor

    # 1. Pertama kali tandai, harus berhasil
    result1 = bot.mark_done(1)
    assert result1 == "marked"
    cursor.execute("SELECT completed FROM tugas_kuliah WHERE task_id = 1")
    assert cursor.fetchone()[0] == 1

    # 2. Tandai ulang, harus terdeteksi sebagai sudah selesai
    result2 = bot.mark_done(1)
    assert result2 == "already_done"

    # 3. Coba tandai ID yang tidak ada
    result3 = bot.mark_done(999)
    assert result3 == "not_found"
