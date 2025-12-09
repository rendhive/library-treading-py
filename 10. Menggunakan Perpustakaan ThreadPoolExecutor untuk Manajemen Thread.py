from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(n)
    return f"Task {n} selesai"

with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(task, i) for i in range(1, 5)]

for future in futures:
    print(future.result())

# Fungsi: Menggunakan ThreadPoolExecutor untuk mengelola thread dengan lebih mudah dan efisien.
# Kondisi: Ketika Anda memiliki banyak tugas yang dapat dijalankan secara paralel tanpa harus mengelola threading secara manual.
