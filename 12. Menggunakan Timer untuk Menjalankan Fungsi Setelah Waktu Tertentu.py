import threading

def hello():
    print("Hello, World!")

# Menjalankan fungsi setelah 2 detik
timer = threading.Timer(2.0, hello)
timer.start()

# Fungsi: Menggunakan Timer untuk menjadwalkan eksekusi fungsi setelah waktu tertentu.
# Kondisi: Ketika Anda ingin melakukan delay sebelum menjalankan suatu fungsi atau tugas.
