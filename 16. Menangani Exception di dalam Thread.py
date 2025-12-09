import threading

def risky_task():
    raise ValueError("Something went wrong in the thread!")

try:
    thread = threading.Thread(target=risky_task)
    thread.start()
    thread.join()
except Exception as e:
    print(f"Error caught: {e}")
# Fungsi: Menangani exception yang terjadi dalam thread.
# Kondisi: Ketika Anda perlu memastikan bahwa error dalam thread dapat ditangkap dan ditangani.
