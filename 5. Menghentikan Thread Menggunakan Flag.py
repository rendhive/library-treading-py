import threading
import time

stop_threads = False

def run():
    while not stop_threads:
        print("Thread is running...")
        time.sleep(1)

# Membuat dan menjalankan thread
thread = threading.Thread(target=run)
thread.start()

# Biarkan berjalan selama 3 detik
time.sleep(3)
stop_threads = True  # Menghentikan thread
thread.join()

print("Thread telah dihentikan.")
# Fungsi: Menggunakan flag untuk menghentikan thread dengan kontrol.
# Kondisi: Ketika Anda ingin menghentikan thread melalui kondisi tertentu.
