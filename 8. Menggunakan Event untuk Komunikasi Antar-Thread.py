import threading
import time

event = threading.Event()

def wait_for_event():
    print("Thread menunggu event...")
    event.wait()  # Menunggu event terjadi
    print("Event terjadi! Thread melanjutkan.")

thread = threading.Thread(target=wait_for_event)
thread.start()

time.sleep(2)  # Simulasi pekerjaan
event.set()  # Mengatur event, memberi tanda untuk melanjutkan

thread.join()

# Fungsi: Menggunakan event untuk mengontrol eksekusi thread berdasarkan sinyal dari thread lain.
# Kondisi: Ketika Anda perlu menunggu hingga kondisi tertentu terjadi sebelum melanjutkan eksekusi.
