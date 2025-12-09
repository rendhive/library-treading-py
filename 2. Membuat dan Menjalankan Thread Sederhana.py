import threading
import time

def say_hello():
    print("Hello from thread!")
    
# Membuat dan menjalankan thread
thread = threading.Thread(target=say_hello)
thread.start()
thread.join()  # Menunggu thread selesai

print("Thread selesai dijalankan.")
# Fungsi: Membuat thread untuk menjalankan fungsi secara bersamaan.
# Kondisi: Ketika Anda ingin menjalankan tugas di latar belakang.
