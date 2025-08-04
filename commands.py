from database import get_connection

class TaskBot:
    def __init__(self):
        self.conn, self.cursor = get_connection()

    def add_task(self, judul_tugas):
        self.cursor.execute("INSERT INTO tugas_kuliah (judul_tugas) VALUES (?)", (judul_tugas,))
        self.conn.commit()
        print("Tugas berhasil ditambahkan")

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tugas_kuliah WHERE task_id = ?", (task_id,))
        self.conn.commit()
        print("Tugas berhasil dihapus")

    def mark_done(self, task_id):
        self.cursor.execute("UPDATE tugas_kuliah SET completed = 1 WHERE task_id = ?", (task_id,))
        self.conn.commit()
        print("Tugas Berhasil diselesaikan")
    
    def list_tugas(self):
        self.cursor.execute("SELECT task_id, judul_tugas, completed FROM tugas_kuliah")
        tasks = self.cursor.fetchall()
        return tasks

    def close(self):
        self.conn.close()