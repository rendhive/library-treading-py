import threading
import time

class WebsiteScraper:
    def __init__(self):
        self.lock = threading.Lock()
        self.websites = ["site1.com", "site2.com", "site3.com"]

    def scrape(self, website):
        with self.lock:  # Memastikan hanya satu thread yang mengakses pada satu waktu
            print(f"Scraping {website}...")
            time.sleep(2)
            print(f"Finished scraping {website}")

scraper = WebsiteScraper()
threads = [threading.Thread(target=scraper.scrape, args=(site,)) for site in scraper.websites]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# Fungsi: Menerapkan lock pada resource saat bekerja dengan beberapa thread.
# Kondisi: Ketika Anda ingin mencegah akses bersamaan ke resource yang tidak aman.
