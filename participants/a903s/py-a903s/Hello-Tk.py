#!/usr/bin/env python

from Tkinter import *
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
    tkMessageBox.showinfo ("Hello Python", "Hello World")

L1 = Label (top, text = "User Name")
L1.pack( side = LEFT)

E1 = Entry (top, bd = 5)
E1.pack()

B = Tkinter.Button (top, text = "OK", command = helloCallBack)
B.pack()

top.mainloop()
