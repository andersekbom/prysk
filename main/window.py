#import sys
from Tkinter import *
from time import sleep
import _map
#import tkFileDialog
#import tkMessageBox

def exit_this():
    exit()

def build_map():
    map_button(text='Building map...')
    _map.initMap()
    map_button.text='Done!'
   
# main window
root = Tk()
root.title("Python implementation of Risk")

#buttons
f = Frame(root, pady=5)
f.pack(side=TOP)

map_button = Button(f, text="Build map", command=build_map, width=20)
map_button.pack(side=LEFT, expand=1, padx=5)

exit_button = Button(f, text="Exit", command=exit_this, width=20)
exit_button.pack(side=LEFT, expand=1, padx=5)

#label above board
var = StringVar()
w = Label(root, textvariable=var)
w.pack(side=TOP)

#canvas
render_window = Canvas(root, width=500, height=200)
render_window.pack()

root.mainloop()

