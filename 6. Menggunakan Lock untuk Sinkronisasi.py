import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    for _ in range(10000):
        lock.acquire()
        counter += 1
        lock.release()

# Membuat beberapa thread yang akan mengakses data yang sama
threads = []
for _ in range(2):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Counter:", counter)
# Fungsi: Menggunakan kunci (lock) untuk menghindari race condition pada variabel bersama.
# Kondisi: Ketika beberapa thread harus mengakses atau mengubah data bersama secara aman.
