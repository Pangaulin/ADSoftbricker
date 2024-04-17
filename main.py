import subprocess
import time
import os
from config import adb_path
from zipfile import ZipFile
from modules.login import login
from modules.processManager import processManager

ASCII_ART = '''
   _____  ________    _________       _____  __ ___.         .__        __                 
  /  _  \\ \\______ \\  /   _____/ _____/ ____\\/  |\\_ |_________|__| ____ |  | __ ___________ 
 /  /_\\  \\ |    |  \\ \\_____  \\ /  _ \\   __\\\\   __\\ __ \\_  __ \\  |/ ___\\|  |/ // __ \\_  __ \\
/    |    \\|    `   \\/        (  <_> )  |   |  | | \\_\\ \\  | \\/  \\  \\___|    <\\  ___/|  | \\/
\\____|__  /_______  /_______  /\\____/|__|   |__| |___  /__|  |__|\\___  >__|_ \\\\___  >__|   
        \\/        \\/        \\/                       \\/              \\/     \\/    \\/ By Pangaulin
'''

print(ASCII_ART)
time.sleep(2)

if __name__ == "__main__":
    try:
        if not os.path.exists('modules\\platform-tools'):
            print("Downloading Android Debug Bridge")
            subprocess.run(["curl", "https://dl.google.com/android/repository/platform-tools-latest-windows.zip?hl=fr", "-o", "modules\\platform-tools.zip"])
            with ZipFile('modules\\platform-tools.zip', 'r') as zip:
                zip.extractall(path="modules")
            os.remove("modules\\platform-tools.zip")

        print("How do you want to connect to device ?")
        print("USB Debug (1)")
        print("Wireless Debug (2)")
        while True:
            try:
                loginMethod = input("Enter a number: ")
                loginMethod = int(loginMethod)
                if loginMethod != 1 and loginMethod != 2:
                    print("Invalid input. Please enter a valid number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            
        login(loginMethod)

        process = subprocess.run([adb_path, "shell", "pm", "list", "packages", "-f"], capture_output=True, text=True, shell=False, check=False)
        process_list = process.stdout.split('\n')

        processManager().rename(process_list)

        for i in range(len(process_list)):
            processManager().delete(process_list[i])
        
        print('\n')
        subprocess.run([adb_path, "reboot"])
        print("Rebooting the device...")
        print("\n")

        print("Thank you for using this service")
        input("Press ENTER to continue...")
    except KeyboardInterrupt:
        print("\nThank you for using this service")
        input("Press ENTER to continue...")