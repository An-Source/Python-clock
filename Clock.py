import sys
from tkinter import *
import time
import pyfiglet


result = pyfiglet.figlet_format("Clock", font = "slant"  )
print("Version:1.0")
print("Author:An-Source")
print(result)






def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text= time_string)
    clock.after(200,tick)

root = Tk()
clock = Label(root, font = ("times", 50, "bold"), bg="white")
clock.grid(row=0,column=1)
tick()
root.mainloop()

