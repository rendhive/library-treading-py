import threading
import time

def display_thread_name():
    print(f"Nama thread: {threading.current_thread().name}")

# Membuat dan menjalankan thread
thread = threading.Thread(target=display_thread_name)
thread.start()
thread.join()

# Fungsi: Menggunakan current_thread() untuk mendapatkan nama thread yang sedang berjalan.
# Kondisi: Ketika Anda perlu mendapatkan informasi tentang thread yang sedang eksekusi.
