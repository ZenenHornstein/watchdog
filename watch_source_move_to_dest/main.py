

#!/usr/bin/python3
"""
This program takes two arguments a directory to monitor and a destination to diretory. Files created in the monitored direction are moved to the destination directory
"""
import os
import sys
#import logging
import argparse
import time
from watchdog.observers import Observer
#from watchdog.events import PatternMatchingEventHandler
from watchdog.events import FileSystemEventHandler

parser = argparse.ArgumentParser(description='Monitor a directory for new files and move them to a destination dir')
parser.add_argument('Source Directory', metavar='SOURCE', type=str,  help='The directory you would like to monitor for new files')
parser.add_argument('Destination Directory', metavar='DEST', type=str,  help='The directory the files will be moved too')
args = parser.parse_args()
 

DIR_TO_WATCH = sys.argv[1]
DESTINATION_DIR = sys.argv[2]


def move_file(file_path, dest_dir):
    print(f"Moving '{file_path}' To  {dest_dir}")
    os.system(f"mv '{file_path}' {dest_dir}")
   #Consider Swapping this for a OS agnostic method see shutil.move



class MyHandler(FileSystemEventHandler):
    """Handles filesystem event"""
    def on_created(self, event):
        move_file(event.src_path, DESTINATION_DIR)

def main():
    print(f"Watching: {DIR_TO_WATCH}")
    print(f"Destination: {DESTINATION_DIR}")
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, DIR_TO_WATCH)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()

