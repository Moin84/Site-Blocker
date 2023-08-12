from tkinter import *
import sys

window = Tk()
window.title("Fushhhhh")
window.geometry("1x1")

T = Label(window, text="Close it", font=("consolas", 12, "bold")).place(x=20, y=0)

hosts_path = "C:\Windows\System32\drivers\etc\hosts"
file_path = "D:\Projects\Project Files\SiteBlocker\in1.txt"
ip = "0.0.0.0"

with open(hosts_path, "r") as hr_file:
    file_content = hr_file.readlines()

with open(file_path, "r") as fr_file:
    webs = fr_file.readline()
websites = list(webs.split(", "))

with open(hosts_path, "w") as w_file:
    for line in file_content:
        ok = True
        for website in websites:
            if ip+" www."+website == line.strip("\n") or ip+" "+website == line.strip("\n"):
                ok = False
                break
        if ok:
            w_file.write(line)

sys.exit()
window.mainloop()