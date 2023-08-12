from tkinter import *
import os, sys

window = Tk()
window.title("Fushhhhh")
window.geometry("1x1")

T = Label(window, text="Close it", font=("consolas", 12, "bold")).place(x=20, y=0)

file_path = "D:\Projects\Project Files\SiteBlocker\in2.txt"

with open(file_path, "r") as fr_file:
    webs = fr_file.readline()
websites = list(webs.split(", "))


ok = ""
def proxy(serverAddress, port):
    os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d ' + serverAddress + ':' + port + ' /f')

os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f')
proxy("0.0.0.0", "80")

if len(websites) != 0:
    i = 0
    for website in websites:
        if i != 0:
            ok = ok +";"
        ok = ok + website
        i = i+1
    os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyOverride /t REG_SZ /d '+ ok +' /f')

sys.exit()
window.mainloop()