from commands import TaskBot

def main():
    bot = TaskBot()
    while True:
        print("Apa yang anda bisa lakukan? menambah, menghapus, menandai, melihat list, keluar")
        tombol = input("Apa yang ingin anda lakukan? ").strip().lower()
        if tombol == "menambah":
            desc = input("Deskripsikan tugas: ")
            bot.add_task(desc)
        elif tombol == "menghapus" :
            try:
                tid = int(input("Masukkan ID tugas yang ingin dihapus: "))
                bot.delete_task(tid)  
            except ValueError:
                print("ID tidak ditemukan")
        elif tombol == "menandai":
            try:
                tid = int(input("Masukkan ID Tugas yang ingin ditandai: "))
                bot.mark_done(tid)
            except ValueError:
                print ("ID tidak ditemukan")
        elif tombol == "melihat list":
            bot.list_tugas()
        elif tombol == "keluar":
            bot.close()
            print ("Terima Kasih, sampai jumpa")
            break
        else:
            print("perintah tidak ditemukan") 

if __name__ == "__main__":
    main()   