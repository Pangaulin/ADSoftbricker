#   _____  ________    _________       _____  __ ___.         .__        __
#  /  _  \ \______ \  /   _____/ _____/ ____\/  |\_ |_________|__| ____ |  | _ _ ___________
# /  /_\  \ |    |  \ \_____  \ /  _ \   __\\   __\ __ \_  __ \  |/ ___\|  |/ // __ \_  __ \
#\____|__  /_______  /_______  /\____/|__|   |__| |___  /__|  |__|\___  >__|_ \\___  >__|
#        \/        \/        \/                       \/              \/     \/    \/  By Pangaulin

import subprocess
from modules.login import loginProcess
from modules.array import package_remover
from modules.deleteProcess import deleteProcess

loginProcess().login()

process = subprocess.run(["adb", "shell", "cmd", "package", "list", "packages"], capture_output=True, text=True, shell=True, check=False)
process_list = process.stdout.split('\n')

package_remover(process_list)

for i in range(len(process_list)):
    deleteProcess(process_list[i])

subprocess.run(["adb", "reboot"])

print("Thank you for using this service")
input("Press a key to continue...")
