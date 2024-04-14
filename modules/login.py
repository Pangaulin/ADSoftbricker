"""Function designed to facilitate the connection to an Android device using ADB (Android Debug Bridge), either via USB or over a network connection."""
import subprocess
import re
from config import adb_path

def login(method):
    if method == 1:
        print("Please check your device is connected in USB, and if USB debug is activated on your phone")
        input("Press ENTER when it's done...")
    
    if method == 2:
        regex_ip = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        regex_port = r'^([0-9]|[1-9][0-9]{1,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$'

        while True:
            try:
                is_paired = input("Is your device paired with ADB ? (y / n) : ")
                is_paired = is_paired.lower()
                if is_paired != "y" and is_paired != "n":
                    print("Invalid input. Please enter a valid choice.")
                else:
                    match is_paired:
                        case "y":
                            is_paired = True
                        case "n":
                            is_paired = False
                    break
            except ValueError:
                print("Invalid input. Please enter a valid choice.")

        if is_paired == False:
            while True:
                device_pair_ip = input('Device pairing IP (Generally as XXX.XXX.X.XX): ')
                if not re.match(regex_ip, device_ip):
                    print("The IP adress isn't valid")
                else:
                    break
            while True:
                device_pair_port = input('Device pair port (Generally as XXXXX) : ')
                if not re.match(regex_port, device_port):
                    print("The port isn't a valid port")
                else:
                    break

            pair_return = subprocess.run([adb_path, 'pair', f'{device_pair_ip}:{device_pair_port}'], shell=True, capture_output=True, text=True)
            print(pair_return.stdout)

        while True:
            if is_paired == True:
                device_ip = input('Device IP (Generally as XXX.XXX.X.XX): ')
            else:
                device_ip = input('Device IP (not the same as Device Pair IP) (Generally as XXX.XXX.X.XX): ')
            if not re.match(regex_ip, device_ip):
                print("The IP adress isn't valid")
            else:
                break

        while True:
            if is_paired == True:
                device_port = input('Device port (Generally as XXXXX) : ')
            else:
                device_port = input('Device port (not the same as Device Pair port) (Generally as XXXXX) : ')
            if not re.match(regex_port, device_port):
                   print("The port isn't a valid port")
            else:
                break

        connect_return = subprocess.run([adb_path, 'connect', f'{device_ip}:{device_port}'], shell=False, capture_output=True, text=True)
        if "cannot connect" in connect_return.stdout:
            print("An error has occured while connecting to the device, please check the IP adress and the device port")
            input("Please press ENTER to continue...")
            exit()