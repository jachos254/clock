import time
import tkinter
import random
from icon import icon
from tkinter import PhotoImage
import base64

def random_int():
    number = random.randint(1,255)
    return number

def rgb2hex(r,g,b):
    hex = '{:02x}{:02x}{:02x}'.format(r,g,b)
    return hex

def clock():
    time_live = time.strftime('%H:%M:%S')
    label.config(text=time_live)
    label.after(100, clock)

window = tkinter.Tk()
icon = base64.b64decode(icon)
icon = PhotoImage(data=icon)
window.title(' ')
# window.geometry('310x100')
window.resizable(False, False)

font = ('Digital Dismay',68)

# black = '#230b0b'
black = '#230B0B'
red = '#df091a'
color_1 = '#' + (rgb2hex(random_int(), random_int(), random_int()))
color_2 = '#' + (rgb2hex(random_int(), random_int(), random_int()))

# label = tkinter.Label(window, font = font, fg = red, bg = black)
label = tkinter.Label(window, font = font, fg = color_1, bg = color_2)
label.grid(row=0, column=1)



clock()
# window.iconbitmap('clock.ico')
window.wm_iconphoto(True, icon)
window.mainloop()