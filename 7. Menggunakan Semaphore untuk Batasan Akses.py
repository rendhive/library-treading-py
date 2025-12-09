import threading
import time

semaphore = threading.Semaphore(2)  # Hanya 2 thread yang dapat mengakses
def access_resource(thread_number):
    print(f"Thread {thread_number} menunggu akses...")
    with semaphore:
        print(f"Thread {thread_number} memiliki akses!")
        time.sleep(2)
    print(f"Thread {thread_number} selesai.")

# Membuat beberapa thread
threads = []
for i in range(5):
    thread = threading.Thread(target=access_resource, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Fungsi: Menggunakan semaphore untuk membatasi jumlah thread yang dapat mengakses resource bersamaan.
# Kondisi: Ketika Anda memiliki resource yang tidak dapat diakses secara bersamaan oleh semua thread.
