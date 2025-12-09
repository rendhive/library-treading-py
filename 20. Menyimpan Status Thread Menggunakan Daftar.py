import threading
import time

status_list = []

def worker(thread_name):
    print(f"{thread_name} mulai bekerja...")
    status_list.append((thread_name, "In Progress"))
    time.sleep(2)
    status_list.append((thread_name, "Completed"))
    print(f"{thread_name} selesai!")

threads = []
for i in range(3):
    thread_name = f"Thread-{i+1}"
    thread = threading.Thread(target=worker, args=(thread_name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Status semua thread:", status_list)
# Fungsi: Menyimpan status dari setiap thread dalam daftar.
# Kondisi: Ketika Anda ingin melacak status eksekusi beberapa thread secara bersamaan.
