

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
#    patterns = "*"
#    ignore_patterns = ""
#    ignore_directories = False
#    case_sensitive = True
#    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
#    my_event_handler.on_any_event
#    path=sys.argv[1]
#    go_recursively = False
#    my_observer = Observer()
#    my_observer.schedule(my_event_handler, path, recursive=go_recursively)    
#
#    my_observer.start()
#    try:
#        while True:
#            time.sleep(1)
#    except KeyboardInterrupt:
#        my_observer.stop()
#        my_observer.join()
