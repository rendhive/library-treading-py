import threading
import time

event = threading.Event()

def worker():
    print("Worker menunggu...")
    event.wait()  # Menunggu sampai event diset
    print("Worker dilanjutkan!")

thread = threading.Thread(target=worker)
thread.start()

time.sleep(2)  # Simulasi pekerjaan lain
event.set()  # Sinyal worker untuk melanjutkan

# Fungsi: Menggunakan Event untuk mengontrol eksekusi thread berdasarkan kondisi yang dinyatakan.
# Kondisi: Ketika Anda perlu menunggu sinyal tertentu sebelum melanjutkan eksekusi dalam thread.
