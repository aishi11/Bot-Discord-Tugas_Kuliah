import sqlite3

def get_connection(db_name="tugas_kuliah.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tugas_kuliah (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            judul_tugas TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0         
        )
    ''')
    conn.commit()
    return conn, cursor