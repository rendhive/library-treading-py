import threading
import time

def io_bound_task():
    print("Mulai I/O bound task...")
    time.sleep(5)  # Simulasi pengambilan data
    print("I/O bound task selesai.")

threads = []
for _ in range(3):
    thread = threading.Thread(target=io_bound_task)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Fungsi: Menjalankan operasi I/O bound dengan menggunakan threads.
# Kondisi: Ketika Anda memiliki tugas yang memerlukan waktu tunggu (I/O), sehingga memungkinkan thread lain untuk berjalan.
