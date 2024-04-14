"""This class provides functionality to delete all the Android applications using ADB commands."""
import subprocess
from config import adb_path

class processManager():
    def rename(self, array):
        for i in range(len(array)):
            if array[i].startswith('package:'):
                array[i] = array[i][len('package:'):]
        return array

    def delete(self, process):
        subprocess.run([adb_path, "shell", "pm", "uninstall", "-k", "--user", "0" , f"{process}"])
        return print(f'{process} was successfully deleted !')