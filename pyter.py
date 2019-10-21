from tkinter import *
import requests

root = Tk()
root.title("Pyter")

data = eval(requests.get("http://localhost:5000/metrics").text)
cpu = Label(root, text="CPU Load: {}%".format(data['cpu']))
cpu.pack()
disk = Label(root, text="Disk", fg="black", bg="yellow")
disk.pack(fill=X)
disk_total = Label(root, text="Total: {} {}".format(data['disk']['total']['size'], data['disk']['total']['unit']), fg="black", bg="yellow")
disk_total.pack(fill=X)
disk_free = Label(root, text="Free: {} {}".format(data['disk']['free']['size'], data['disk']['free']['unit']), fg="black", bg="yellow")
disk_free.pack(fill=X)
up_time = Label(root, text="Up time: {} {}".format(data['up_time']['time'], data['up_time']['unit']))
up_time.pack()

root.mainloop()