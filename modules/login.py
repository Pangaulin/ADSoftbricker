import subprocess
import time
import re

ASCII_ART = '''
   _____  ________    _________       _____  __ ___.         .__        __                 
  /  _  \\ \\______ \\  /   _____/ _____/ ____\\/  |\\_ |_________|__| ____ |  | __ ___________ 
 /  /_\\  \\ |    |  \\ \\_____  \\ /  _ \\   __\\\\   __\\ __ \\_  __ \\  |/ ___\\|  |/ // __ \\_  __ \\
/    |    \\|    `   \\/        (  <_> )  |   |  | | \\_\\ \\  | \\/  \\  \\___|    <\\  ___/|  | \\/
\\____|__  /_______  /_______  /\\____/|__|   |__| |___  /__|  |__|\\___  >__|_ \\\\___  >__|   
        \\/        \\/        \\/                       \\/              \\/     \\/    \\/ By Pangaulin
'''

class loginProcess():
    def login(self):
        print(ASCII_ART)
        time.sleep(2)

        while True:
            print("What method are you using to connect to the device ?")
            print("USB Debugging (1)")
            print("Wireless Debugging (2)")
            loginMethod = input("Your choice : ")
            loginMethod = int(loginMethod)
            if loginMethod == 1 or loginMethod == 2:
                break
            else:
                print("Incorrect input !")
                print('\n')
        if loginMethod == 1:
            print()
        if loginMethod == 2:
            self.wirelessLogin()

    def usbLogin(self):
        print("Unsupported for the moment")

    def wirelessLogin(self):
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

        subprocess.run(["adb", 'connect', f'{device_ip}:{device_port}'], shell=True, check=False)