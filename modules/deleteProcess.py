import subprocess

def deleteProcess(process):
    subprocess.run(["adb", "shell", "pm", "uninstall", "-k", "--user", "0" , f"{process}"])
    return print(f'{process} was successfully deleted !')