import time
import tkinter
import random

window = tkinter.Tk()
window.title(' ')
# window.geometry('310x100')
window.resizable(False, False)

font = ('Digital Dismay',68)

black = '#230b0b'
red = '#df091a'

label = tkinter.Label(window, font = font, fg = red, bg = black)
label.grid(row=0, column=1)

def clock():
    time_live = time.strftime('%H:%M:%S')
    label.config(text=time_live)
    label.after(100, clock)

clock()
window.iconbitmap('clock.ico')
window.mainloop()