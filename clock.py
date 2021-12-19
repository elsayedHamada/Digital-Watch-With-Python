from tkinter import *
from tkinter.ttk import *
from time import strftime

# Create Window
WINDOW = Tk()
WINDOW.title("Clock")
WINDOW.config(background="black")
WINDOW.geometry("800x100")
# get time
def getTime():
    time = strftime("%H:%M:%S %p")
    label.config(text=time)
    label.after(1000, getTime)

label = Label(WINDOW, font=("ds-digital", 80), background="black", foreground="purple")
label.pack(anchor="center")

getTime()

mainloop()