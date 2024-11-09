import win32file
import win32api
import time
from ctypes import wintypes
import subprocess
import os

os.system('cls')
# Define constants
DBT_DEVICEARRIVAL = 0x8000  
DBT_DEVTYP_VOLUME = 0x00000002  
WM_DEVICECHANGE = 0x0219  


def get_drive_letter():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\x00')[:-1]
    usb_drives = []
    for drive in drives:
        try:
            if win32file.GetDriveType(drive) == win32file.DRIVE_REMOVABLE:
                usb_drives.append(drive)
        except Exception as e:
            print(f"Error accessing drive {drive}: {e}")
    return usb_drives


def monitor_usb():
    print("Listening for USB device connections on Windows...")
    existing_usb_drives = set(get_drive_letter())

    while True:
        current_usb_drives = set(get_drive_letter())
        new_drives = current_usb_drives - existing_usb_drives
        if new_drives:
            for drive in new_drives:
                print(f"New USB device connected: {drive}")
                if drive[0] == "F":
                    print("stick inserted")
                    subprocess.run(["python", "C:\python\python_codes\enter.py"])


        time.sleep(5)

monitor_usb()