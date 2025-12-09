import threading
import time

def task(n):
    print(f"Task {n} dimulai.")
    time.sleep(2)
    print(f"Task {n} selesai.")

threads = []
for i in range(3):
    thread = threading.Thread(target=task, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()  # Menunggu semua thread selesai

print("Semua task telah selesai.")
# Fungsi: Menunggu semua thread selesai sebelum melanjutkan.
# Kondisi: Ketika Anda ingin menunggu penyelesaian beberapa thread sebelum meneruskan eksekusi.
