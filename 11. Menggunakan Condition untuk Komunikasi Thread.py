import threading
import time

condition = threading.Condition()
data_ready = False

def consumer():
    with condition:
        while not data_ready:
            condition.wait()
        print("Data telah dikonsumsi.")

def producer():
    time.sleep(2)  # Simulasi waktu untuk memproduksi data
    global data_ready
    with condition:
        data_ready = True
        condition.notify()

# Membuat dan menjalankan producer dan consumer
thread_producer = threading.Thread(target=producer)
thread_consumer = threading.Thread(target=consumer)

thread_consumer.start()
thread_producer.start()

thread_consumer.join()
thread_producer.join()

# Fungsi: Menggunakan condition untuk menunggu dan memberi tahu antar-thread.
# Kondisi: Ketika Anda perlu mengoordinasikan kegiatan antara producer dan consumer.
