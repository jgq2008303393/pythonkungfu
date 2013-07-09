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

        self.seven = Button(self.parent, text="7", font=self.helv12, command=self.seven)
        self.seven.grid(row=1, column=0)

        self.eight = Button(self.parent, text="8", font=self.helv12, command=self.eight)
        self.eight.grid(row=1, column=1)

        self.nine = Button(self.parent, text="9", font=self.helv12, command=self.nine)
        self.nine.grid(row=1, column=2)

        self.four = Button(self.parent, text="4", font=self.helv12, command=self.four)
        self.four.grid(row=2, column=0)

        self.five = Button(self.parent, text="5", font=self.helv12, command=self.five)
        self.five.grid(row=2, column=1)

        self.six = Button(self.parent, text="6", font=self.helv12, command=self.six)
        self.six.grid(row=2, column=2)

        self.one = Button(self.parent, text="1", font=self.helv12, command=self.one)
        self.one.grid(row=3, column=0)

        self.two = Button(self.parent, text="2", font=self.helv12, command=self.two)
        self.two.grid(row=3, column=1)

        self.three = Button(self.parent, text="3", font=self.helv12, command=self.three)
        self.three.grid(row=3, column=2)

        self.zero = Button(self.parent, text="0", font=self.helv12, command=self.zero)
        self.zero.grid(row=1, column=3)

        self.minus = Button(self.parent, text="-", font=self.helv12, command=self.minus)
        self.minus.grid(row=2, column=3)

        self.divide = Button(self.parent, text="/", font=self.helv12, command=self.divide)
        self.divide.grid(row=3, column=3)

        self.times = Button(self.parent, text="*", font=self.helv12, command=self.times)
        self.times.grid(row=1, column=4)

        self.plus = Button(self.parent, text="+", font=self.helv12, command=self.plus)
        self.plus.grid(row=2, column=4)

        self.equals = Button(self.parent, text="=", font=self.helv12, command=self.equals)
        self.equals.grid(row=3, column=4)

    def one(self):
        self.temp += "1"
        self.mainLabel['text'] = self.temp

    def two(self):
        self.temp += "2"
        self.mainLabel['text'] = self.temp

    def three(self):
        self.temp += "3"
        self.mainLabel['text'] = self.temp

    def four(self):
        self.temp += "4"
        self.mainLabel['text'] = self.temp

    def five(self):
        self.temp += "5"
        self.mainLabel['text'] = self.temp

    def six(self):
        self.temp += "6"
        self.mainLabel['text'] = self.temp

    def seven(self):
        self.temp += "7"
        self.mainLabel['text'] = self.temp

    def eight(self):
        self.temp += "8"
        self.mainLabel['text'] = self.temp

    def nine(self):
        self.temp += "9"
        self.mainLabel['text'] = self.temp

    def zero(self):
        self.temp += "0"
        self.mainLabel['text'] = self.temp

    def plus(self):
        self.temp += " + "
        self.mainLabel['text'] = self.temp

    def minus(self):
        self.temp += " - "
        self.mainLabel['text'] = self.temp

    def divide(self):
        self.temp += " / "
        self.mainLabel['text'] = self.temp

    def times(self):
        self.temp += " * "
        self.mainLabel['text'] = self.temp

    def equals(self):
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
