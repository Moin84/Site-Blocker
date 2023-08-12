import os, sys
from tkinter import *

window = Tk()
window.title("Fushhhhh")
window.geometry("1x1")

T = Label(window, text="Close it", font=("consolas", 12, "bold")).place(x=20, y=0)

file_path = "D:\Projects\Project Files\SiteBlocker\in2.txt"

with open(file_path, "r") as fr_file:
    webs = fr_file.readline()
websites = list(webs.split(", "))


def proxy(serverAddress, port):
    os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d ' + serverAddress + ':' + port + ' /f')

os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f')
proxy("0.0.0.0", "80")

sys.exit()
window.mainloop()
