from database import get_connection

class TaskBot:
    def __init__(self):
        self.conn, self.cursor = get_connection()

    def add_task(self, judul_tugas):
        self.cursor.execute("SELECT task_id FROM tugas_kuliah ORDER BY task_id ASC")
        existing_ids = [row[0] for row in self.cursor.fetchall()]

        task_id = 1
        for id in existing_ids:
            if id != task_id:
                break
            task_id += 1

        self.cursor.execute("INSERT INTO tugas_kuliah (task_id, judul_tugas) VALUES (?, ?)", (task_id, judul_tugas))
        self.conn.commit()

        return {"task_id": task_id, "judul_tugas": judul_tugas}
    
    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tugas_kuliah WHERE task_id = ?", (task_id,))
        if self.cursor.rowcount == 0:
            return False
        self.conn.commit()
        return True

    def mark_done(self, task_id):
        self.cursor.execute("UPDATE tugas_kuliah SET completed = 1 WHERE task_id = ?", (task_id,))
        if self.cursor.rowcount == 0:
            return False
        self.conn.commit()
        return True
    
    def list_tugas(self):
        self.cursor.execute("SELECT * FROM tugas_kuliah")
        tasks = self.cursor.fetchall()
        return tasks

    def close(self):
        self.conn.close()