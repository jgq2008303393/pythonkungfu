#!/usr/bin/env python

from Tkinter import *
import tkMessageBox


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Simple")

        self.label = Label(self.parent, text="Hello World", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2)

        self.userLabel = Label(self.parent, text="User Name")
        self.userLabel.grid(row=1, column=0)

        self.userEntry = Entry(self.parent, bd=1)
        self.userEntry.grid(row=1, column=1)

        self.passwordLabel = Label(self.parent, text="Password")
        self.passwordLabel.grid(row=2, column=0)

        self.passwordEntry = Entry(self.parent, bd=1, show="*")
        self.passwordEntry.grid(row=2, column=1)

        self.loginButton = Button(self.parent, text="Login", command=self.login)
        self.loginButton.grid(row=3, column=0)

        self.quitButton = Button(self.parent, text="Quit", command=self.quitCallBack)
        self.quitButton.grid(row=3, column=1, sticky=E+W)

    def quitCallBack(self):
        self.parent.destroy()

    def helloCallBack(self):
        tkMessageBox.showinfo("Hello Python", "Hello World")

    def login(self):
        username = self.userEntry.get()
        password = self.passwordEntry.get()
        if username == "root" and password == "toor":
            tkMessageBox.showinfo("Success", "Hello root")
        else:
            tkMessageBox.showinfo("Fail", "Wrong username and / or password")


def main():
    root = Tk()
    Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
