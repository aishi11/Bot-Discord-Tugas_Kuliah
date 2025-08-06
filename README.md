# Bot-Discord-Tugas_Kuliah
Project Bot discord yang berfungsi untuk manajemen tugas kuliah

## 📦 Fitur Utama
- Menambahkan tugas kuliah
- Melihat daftar tugas
- Menghapus atau menandai tugas sebagai selesai


## 🛠️ Instalasi

1. **Clone Repository**

```bash
git clone https://github.com/aishi11/Bot-Discord-Tugas_Kuliah.git
cd Bot-Discord-Tugas_Kuliah 
```
2. Buat dan isi file .env dengan token bot Discord kamu:
```env
DISCORD_TOKEN=token_bot_discord_kamu
```
3. Install Depedensi
```bash
pip install -r requirements.txt
```
4. Jalankan Bot
```bash
python discord_bot.py
```
# ⚠️ Catatan
Pastikan intents.message_content = True diaktifkan pada bot dan dashboard Discord Developer Portal.

# 💡 Contoh Perintah Discord
1. !add_task <deskripsi_tugas> = menambahkan tugas dengan menuliskan judul atau deksripsi tugas
```bash
!add_task tugas algoritma dan struktur data 5 soal di e-learning
```
2. !delete_task <task_id> = menghapus tugas berdasarkan id tugas
```bash
!delete_task 2
```
3. !complete_task <task_id> = menandai tugas yang sudah selesai dikerjakan berdasarkan id tugas
```bash
!complete_task 1
```
4. !show_tasks = melihat daftar atau list tugas
```bash
!show_tasks
```


