import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print("Thread kustom sedang berjalan...")
        time.sleep(2)
        print("Thread kustom telah selesai.")

# Membuat dan menjalankan thread kustom
thread = MyThread()
thread.start()
thread.join()

# Fungsi: Membuat thread dengan menggunakan kelas yang diwarisi dari `threading.Thread`.
# Kondisi: Ketika Anda memerlukan kontrol lebih atau ingin menambahkan fungsionalitas khusus ke thread.
