import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print("🔁 Code changed. Restarting...")
            os.system("pkill -f manage.py && python manage.py runserver &")

observer = Observer()
observer.schedule(ReloadHandler(), path=".", recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
