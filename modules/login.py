import subprocess
import re
from config import adb_path

def login(method):
    if method == 1:
        print("Unsupported")
        input("Please press ENTER to continue...")
        exit()
    
    if method == 2:
        regex_ip = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        regex_port = r'^([0-9]|[1-9][0-9]{1,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$'

        while True:
            device_ip = input('Device IP (Generally as XXX.XXX.X.XX): ')
            if not re.match(regex_ip, device_ip):
                print("The IP adress isn't valid")
            else:
                break

        while True:
            device_port = input('Device port (Generally as XXXXX) : ')
            if not re.match(regex_port, device_port):
                   print("The port isn't a valid port")
            else:
                break

        connect_return = subprocess.run([adb_path, 'connect', f'{device_ip}:{device_port}'], shell=False, capture_output=True, text=True, check=False)
        if "cannot connect" in connect_return.stdout:
            print("An error has occured while connecting to the device, please check the IP adress and the device port")
            input("Please press ENTER to continue...")
            exit()