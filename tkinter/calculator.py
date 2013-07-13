#!/usr/bin/env python

from Tkinter import *
import tkFont


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.temp = ""
        self.parent = parent
        self.parent.title("Calculator")
        self.helv16 = tkFont.Font(family="Helvetica", size=16)
        self.helv12 = tkFont.Font(family="Helvetica", size=12)

        self.mainLabel = Label(self.parent, text="0.0", font=self.helv16)
        self.mainLabel.grid(row=0, column=0, columnspan=5)

        self.seven = Button(self.parent, text="7", font=self.helv12, command=lambda: self.numCallback("7"))
        self.seven.grid(row=1, column=0)

        self.eight = Button(self.parent, text="8", font=self.helv12, command=lambda: self.numCallback("8"))
        self.eight.grid(row=1, column=1)

        self.nine = Button(self.parent, text="9", font=self.helv12, command=lambda: self.numCallback("9"))
        self.nine.grid(row=1, column=2)

        self.four = Button(self.parent, text="4", font=self.helv12, command=lambda: self.numCallback("4"))
        self.four.grid(row=2, column=0)

        self.five = Button(self.parent, text="5", font=self.helv12, command=lambda: self.numCallback("5"))
        self.five.grid(row=2, column=1)

        self.six = Button(self.parent, text="6", font=self.helv12, command=lambda: self.numCallback("6"))
        self.six.grid(row=2, column=2)

        self.one = Button(self.parent, text="1", font=self.helv12, command=lambda: self.numCallback("1"))
        self.one.grid(row=3, column=0)

        self.two = Button(self.parent, text="2", font=self.helv12, command=lambda: self.numCallback("2"))
        self.two.grid(row=3, column=1)

        self.three = Button(self.parent, text="3", font=self.helv12, command=lambda: self.numCallback("3"))
        self.three.grid(row=3, column=2)

        self.zero = Button(self.parent, text="0", font=self.helv12, command=lambda: self.numCallback("0"))
        self.zero.grid(row=1, column=3)

        self.minus = Button(self.parent, text="-", font=self.helv12, command=lambda: self.operationCallback("-"))
        self.minus.grid(row=2, column=3)

        self.divide = Button(self.parent, text="/", font=self.helv12, command=lambda: self.operationCallback("/"))
        self.divide.grid(row=3, column=3)

        self.times = Button(self.parent, text="*", font=self.helv12, command=lambda: self.operationCallback("*"))
        self.times.grid(row=1, column=4)

        self.plus = Button(self.parent, text="+", font=self.helv12, command=lambda: self.operationCallback("+"))
        self.plus.grid(row=2, column=4)

        self.equals = Button(self.parent, text="=", font=self.helv12, command=self.equalsCallback)
        self.equals.grid(row=3, column=4)

        self.parent.bind("<Key 1>", lambda x: self.numCallback("1"))
        self.parent.bind("<Key 2>", lambda x: self.numCallback("2"))
        self.parent.bind("<Key 3>", lambda x: self.numCallback("3"))
        self.parent.bind("<Key 4>", lambda x: self.numCallback("4"))
        self.parent.bind("<Key 5>", lambda x: self.numCallback("5"))
        self.parent.bind("<Key 6>", lambda x: self.numCallback("6"))
        self.parent.bind("<Key 7>", lambda x: self.numCallback("7"))
        self.parent.bind("<Key 8>", lambda x: self.numCallback("8"))
        self.parent.bind("<Key 9>", lambda x: self.numCallback("9"))
        self.parent.bind("<Key 0>", lambda x: self.numCallback("0"))
        self.parent.bind("<Key plus>", lambda x: self.operationCallback("+"))
        self.parent.bind("<Key minus>", lambda x: self.operationCallback("-"))
        self.parent.bind("<Key asterisk>", lambda x: self.operationCallback("*"))
        self.parent.bind("<Key slash>", lambda x: self.operationCallback("/"))
        self.parent.bind("<Return>", lambda x: self.equalsCallback())
        self.parent.bind("<BackSpace>", lambda x: self.clear())
        self.parent.bind("<Escape>", lambda x: self.quitGracefully())

    def numCallback(self, args):
        self.temp += str(args)
        self.mainLabel['text'] = self.temp

    def operationCallback(self, args):
        self.temp += " " + str(args) + " "
        self.mainLabel['text'] = self.temp

    def clear(self):
        self.temp = ""
        self.mainLabel['text'] = "0.0"

    def quitGracefully(self):
        self.parent.destroy()

    def equalsCallback(self):
        string = str(self.temp)
        if string.split(" ")[1] == "+":
            result = float(string.split(" ")[0]) + float(string.split(" ")[2])
            result = str(result)
        if string.split(" ")[1] == "-":
            result = float(string.split(" ")[0]) - float(string.split(" ")[2])
            result = str(result)
        if string.split(" ")[1] == "/":
            result = float(string.split(" ")[0]) / float(string.split(" ")[2])
            result = str(result)
        if string.split(" ")[1] == "*":
            result = float(string.split(" ")[0]) * float(string.split(" ")[2])
            result = str(result)
        else:
            self.temp = "NaN"
        self.mainLabel['text'] = result


def main():
    root = Tk()
    Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
