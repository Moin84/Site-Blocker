from tkinter import *
import sys

window = Tk()
window.title("")
window.geometry("1x20")

T = Label(window, text="Close it", font=("consolas", 12, "bold")).place(x=20, y=0)


hosts_path = "C:\Windows\System32\drivers\etc\hosts"
file_path = "D:\Projects\Project Files\SiteBlocker\in1.txt"
ip = "0.0.0.0"

with open(hosts_path, "r") as hr_file:
    file_content = hr_file.readlines()

with open(file_path, "r") as fr_file:
    webs = fr_file.readline()
websites = list(webs.split(", "))

with open(hosts_path, "r+") as hosts_file:
    file_content = hosts_file.read()
    for website in websites:
        if website in file_content:
            pass
        else:
            hosts_file.write(ip +" www."+ website +"\n")
            hosts_file.write(ip +" "+ website +"\n")

sys.exit()
window.mainloop()