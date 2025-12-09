import threading
import time

def countdown(n):
    while n > 0:
        print(f"Countdown: {n}")
        n -= 1
        time.sleep(1)
    print("Countdown selesai!")

# Membuat dan menjalankan thread countdown
countdown_thread = threading.Thread(target=countdown, args=(5,))
countdown_thread.start()
countdown_thread.join()

# Fungsi: Membuat countdown timer menggunakan thread.
# Kondisi: Ketika Anda ingin menampilkan countdown tanpa memblokir eksekusi program utama.
