from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import hashlib
import os
from datetime import datetime

LOG_FILE = "logs/activity_log.txt"

SENSITIVE_FILES = [
    "salary.xlsx",
    "employee_data.csv",
    "passwords.txt"
]

def write_log(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

class MonitorHandler(FileSystemEventHandler):

    def on_created(self, event):
        msg = f"[{datetime.now()}] CREATED: {event.src_path}"
        print(msg)
        write_log(msg)

    def on_deleted(self, event):
        msg = f"[{datetime.now()}] DELETED: {event.src_path}"
        print(msg)
        write_log(msg)

    def on_modified(self, event):
        msg = f"[{datetime.now()}] MODIFIED: {event.src_path}"
        print(msg)
        write_log(msg)

    def on_moved(self, event):
        msg = f"[{datetime.now()}] MOVED: {event.src_path} -> {event.dest_path}"
        print(msg)
        write_log(msg)

        filename = os.path.basename(event.dest_path)

        if filename in SENSITIVE_FILES:
            alert = f"ALERT: Sensitive File Moved -> {filename}"
            print(alert)
            write_log(alert)

path = "C:/MonitorFolder"

observer = Observer()
event_handler = MonitorHandler()

observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    observer.stop()

observer.join()