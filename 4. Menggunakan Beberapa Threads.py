import threading
import time

def countdown(n):
    while n > 0:
        print(f"Countdown: {n}")
        n -= 1
        time.sleep(1)

# Membuat beberapa thread
threads = []
for i in range(3):
    thread = threading.Thread(target=countdown, args=(5,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Fungsi: Membuat dan menjalankan beberapa thread secara bersamaan.
# Kondisi: Ketika Anda memiliki tugas yang perlu berjalan secara paralel.
