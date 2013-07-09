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

        self.seven = Button(self.parent, text="7", font=self.helv12, command=lambda: self.sevenCallback(""))
        self.seven.grid(row=1, column=0)

        self.eight = Button(self.parent, text="8", font=self.helv12, command=lambda: self.eightCallback(""))
        self.eight.grid(row=1, column=1)

        self.nine = Button(self.parent, text="9", font=self.helv12, command=lambda: self.nineCallback(""))
        self.nine.grid(row=1, column=2)

        self.four = Button(self.parent, text="4", font=self.helv12, command=lambda: self.fourCallback(""))
        self.four.grid(row=2, column=0)

        self.five = Button(self.parent, text="5", font=self.helv12, command=lambda: self.fiveCallback(""))
        self.five.grid(row=2, column=1)

        self.six = Button(self.parent, text="6", font=self.helv12, command=lambda: self.sixCallback(""))
        self.six.grid(row=2, column=2)

        self.one = Button(self.parent, text="1", font=self.helv12, command=lambda: self.oneCallback(""))
        self.one.grid(row=3, column=0)

        self.two = Button(self.parent, text="2", font=self.helv12, command=lambda: self.twoCallback(""))
        self.two.grid(row=3, column=1)

        self.three = Button(self.parent, text="3", font=self.helv12, command=lambda: self.threeCallback(""))
        self.three.grid(row=3, column=2)

        self.zero = Button(self.parent, text="0", font=self.helv12, command=lambda: self.zeroCallback(""))
        self.zero.grid(row=1, column=3)

        self.minus = Button(self.parent, text="-", font=self.helv12, command=self.minusCallback)
        self.minus.grid(row=2, column=3)

        self.divide = Button(self.parent, text="/", font=self.helv12, command=self.divideCallback)
        self.divide.grid(row=3, column=3)

        self.times = Button(self.parent, text="*", font=self.helv12, command=self.timesCallback)
        self.times.grid(row=1, column=4)

        self.plus = Button(self.parent, text="+", font=self.helv12, command=self.plusCallback)
        self.plus.grid(row=2, column=4)

        self.equals = Button(self.parent, text="=", font=self.helv12, command=self.equalsCallback)
        self.equals.grid(row=3, column=4)

        self.parent.bind("<Key 1>", self.oneCallback)
        self.parent.bind("<Key 2>", self.twoCallback)
        self.parent.bind("<Key 3>", self.threeCallback)
        self.parent.bind("<Key 4>", self.fourCallback)
        self.parent.bind("<Key 5>", self.fiveCallback)
        self.parent.bind("<Key 6>", self.sixCallback)
        self.parent.bind("<Key 7>", self.sevenCallback)
        self.parent.bind("<Key 8>", self.eightCallback)
        self.parent.bind("<Key 9>", self.nineCallback)
        self.parent.bind("<Key 0>", self.zeroCallback)

    def oneCallback(self, args):
        self.temp += "1"
        self.mainLabel['text'] = self.temp

    def twoCallback(self, args):
        self.temp += "2"
        self.mainLabel['text'] = self.temp

    def threeCallback(self, args):
        self.temp += "3"
        self.mainLabel['text'] = self.temp

    def fourCallback(self, args):
        self.temp += "4"
        self.mainLabel['text'] = self.temp

    def fiveCallback(self, args):
        self.temp += "5"
        self.mainLabel['text'] = self.temp

    def sixCallback(self, args):
        self.temp += "6"
        self.mainLabel['text'] = self.temp

    def sevenCallback(self, args):
        self.temp += "7"
        self.mainLabel['text'] = self.temp

    def eightCallback(self, args):
        self.temp += "8"
        self.mainLabel['text'] = self.temp

    def nineCallback(self, args):
        self.temp += "9"
        self.mainLabel['text'] = self.temp

    def zeroCallback(self, args):
        self.temp += "0"
        self.mainLabel['text'] = self.temp

    def plusCallback(self):
        self.temp += " + "
        self.mainLabel['text'] = self.temp

    def minusCallback(self):
        self.temp += " - "
        self.mainLabel['text'] = self.temp

    def divideCallback(self):
        self.temp += " / "
        self.mainLabel['text'] = self.temp

    def timesCallback(self):
        self.temp += " * "
        self.mainLabel['text'] = self.temp

    def equalsCallback(self):
        if self.temp.split(" ")[1] == "+":
            self.temp = float(self.temp.split(" ")[0]) + float(self.temp.split(" ")[2])
        if self.temp.split(" ")[1] == "-":
            self.temp = float(self.temp.split(" ")[0]) - float(self.temp.split(" ")[2])
        if self.temp.split(" ")[1] == "/":
            self.temp = float(self.temp.split(" ")[0]) / float(self.temp.split(" ")[2])
        if self.temp.split(" ")[1] == "*":
            self.temp = float(self.temp.split(" ")[0]) * float(self.temp.split(" ")[2])
        else:
            self.temp = "NaN"
        self.mainLabel['text'] = self.temp


def main():
    root = Tk()
    Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
