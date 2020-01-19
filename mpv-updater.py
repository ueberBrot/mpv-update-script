import subprocess
import ctypes
import sys


def check_for_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except ValueError:
        print("No Admin Priviliges")


if check_for_admin():
    subprocess.call(r"C:\Program Files (x86)\mpv\updater.bat")
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)