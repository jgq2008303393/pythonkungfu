#!/usr/bin/env python

from Tkinter import *
import tkMessageBox
import tkFont


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Login")
        self.helv16 = tkFont.Font(family="Helvetica", size=16)
        self.helv12 = tkFont.Font(family="Helvetica", size=12)

        self.mainLabel = Label(self.parent, text="Login", font=self.helv16)
        self.mainLabel.grid(row=0, column=0, columnspan=2)

        self.userLabel = Label(self.parent, text="User Name", font=self.helv12)
        self.userLabel.grid(row=1, column=0)

        self.userEntry = Entry(self.parent, bd=1, font=self.helv12)
        self.userEntry.grid(row=1, column=1)

        self.passwordLabel = Label(self.parent, text="Password", font=self.helv12)
        self.passwordLabel.grid(row=2, column=0)

        self.passwordEntry = Entry(self.parent, bd=1, show="*", font=self.helv12)
        self.passwordEntry.grid(row=2, column=1)

        self.loginButton = Button(self.parent, text="Let me in", command=self.login, font=self.helv12)
        self.loginButton.grid(row=3, column=0)

        self.quitButton = Button(self.parent, text="Quit", command=self.quitCallBack, font=self.helv12)
        self.quitButton.grid(row=3, column=1, sticky=E+W)

        self.statusLabel = Label(self.parent, text="Status: Not logged in", font=self.helv12, fg="#000")
        self.statusLabel.grid(row=4, column=0, columnspan=2)

    def quitCallBack(self):
        self.parent.destroy()

    def login(self):
        username = self.userEntry.get()
        password = self.passwordEntry.get()
        if username == "root" and password == "toor":
            self.statusLabel["text"] = "Status: Success to log in"
            self.statusLabel["fg"] = "#006B54"
        else:
            self.statusLabel["text"] = "Status: Fail to log in"
            self.statusLabel["fg"] = "#F00"


def main():
    root = Tk()
    Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
