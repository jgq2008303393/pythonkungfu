#!/usr/bin/env python

import gtk
import sys


class Gui(object):
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(300, 300)
        window.set_border_width(10)
        window.set_title("My First GUI Python")
        window.connect("delete_event", lambda w, e: gtk.main_quit())

        box = gtk.VBox(False, 0)
        window.add(box)

        close = gtk.Button(stock=gtk.STOCK_CLOSE)
        close.connect("clicked", lambda w: gtk.main_quit())
        box.add(close)

        box.show()
        window.show()
        close.show()

        return

if __name__ == "__main__":
    try:
        Gui()
        gtk.main()
    except KeyboardInterrupt:
        print "Caught interrupt signal"
        sys.exit(0)
