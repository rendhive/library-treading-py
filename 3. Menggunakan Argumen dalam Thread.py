import threading

def greet(name):
    print(f"Hello, {name}!")

# Membuat dan menjalankan thread
thread = threading.Thread(target=greet, args=("Alice",))
thread.start()
thread.join()

# Fungsi: Menggunakan argumen saat membuat thread.
# Kondisi: Ketika Anda perlu menyampaikan data ke fungsi yang akan dijalankan di thread.
